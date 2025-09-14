# Secrets Cache CDK Example

This project shows how to use [**py-secrets-cache**](https://github.com/rnag/py-secrets-cache) with AWS Lambda, AWS Secrets Manager, and AWS Systems Manager (SSM) Parameter Store — all deployed using the [AWS CDK](https://aws.amazon.com/cdk/).

It creates:

* ✅ A **Secrets Manager secret**
* ✅ An **SSM Parameter**
* ✅ A **Python Lambda** that reads both using `py-secrets-cache`

---

# Getting Started

This project shows how to use [`secrets-cache`](https://pypi.org/project/secrets-cache/) inside an AWS Lambda function, with AWS CDK managing the infrastructure.

## Prerequisites

Before you begin, make sure you have the following installed and configured:

* **AWS Account** → [Sign up here](https://aws.amazon.com/free/) (free tier is enough for this example).
* [**AWS CLI**](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html):

  ```bash
  aws configure
  ```
   (set your access key, secret key, default region).
* [**AWS CDK Toolkit**](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html):

  ```bash
  npm install -g aws-cdk
  ```
* [**Docker**](https://docs.docker.com/get-docker/):

  > CDK uses Docker under the hood to package Lambda dependencies (like `secrets-cache`).

The first time you deploy CDK resources in your AWS account, you’ll also need to bootstrap it:

```bash
cdk bootstrap
```

---

## Setup

Clone the repo and create a virtual environment:

```bash
git clone https://github.com/rnag/secrets-cache-cdk-example.git
cd secrets-cache-cdk-example
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## Deploy

Synthesize the CloudFormation template:

```bash
cdk synth
```

Deploy the stack:

```bash
cdk deploy
```

This will:

* Create a sample secret in **AWS Secrets Manager**
* Create a parameter in **SSM Parameter Store**
* Deploy a Lambda function that uses `secrets-cache` to read them

---


After deployment, invoke the Lambda:

```bash
aws lambda invoke \
  --function-name CdkExampleStack-TestLambda \
  out.json
cat out.json
```

You should see the cached secret/parameter values printed in the response.

## Clean Up

To avoid charges, destroy everything when you’re done:

```bash
cdk destroy
```

---

## Useful CDK Commands

* `cdk ls` → List all stacks
* `cdk diff` → Compare local vs deployed
* `cdk docs` → Open CDK reference
