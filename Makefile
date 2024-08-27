# Load variables from .env if it exists
ifneq (,$(wildcard ./.env))
    include .env
    export
endif

CONFIGURE_SCRIPT = mf_configure.py

TEST_DIR = tests/
TEST_ARGS = --numprocesses=auto

ECR_REGISTRY = $(AWS_ACCOUNT_ID).dkr.ecr.$(AWS_REGION).amazonaws.com
ECR_NAMESPACE = $(CFN_STACK_NAME)
ECR_PATH = $(ECR_REGISTRY)/$(ECR_NAMESPACE)

ECR_PYTORCH_REPO = pytorch-extras
PYTORCH_TAG = 2.4.0-cuda12.4-cudnn9-runtime
ECR_PYTORCH_IMAGE = $(ECR_PATH)/$(ECR_PYTORCH_REPO):$(PYTORCH_TAG)
DOCKER_PYTORCH_DIR = docker/pytorch-extras/


.PHONY: all
all: install configure

.PHONY: install
install:
	poetry install --no-interaction --no-root

.PHONY: configure
configure:
	poetry run python $(CONFIGURE_SCRIPT)

.PHONY: test
test:
	poetry run pytest $(TEST_ARGS) $(TEST_DIR)

.PHONY: clean
clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete

.PHONY: ecr-auth
ecr-auth:
	aws ecr get-login-password --region $(AWS_REGION) | \
		docker login --username AWS --password-stdin $(ECR_REGISTRY)

.PHONY: build-pytorch
build-pytorch:
	docker build \
		--tag $(ECR_PYTORCH_IMAGE) \
		--build-arg PYTORCH_TAG=$(PYTORCH_TAG) \
		$(DOCKER_PYTORCH_DIR)

.PHONY: push-pytorch
push-pytorch: build-pytorch ecr-auth
	docker push $(ECR_PYTORCH_IMAGE)