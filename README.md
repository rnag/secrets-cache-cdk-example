# Secrets Cache CDK Example

This project shows how to use [**py-secrets-cache**](https://github.com/rnag/py-secrets-cache) with AWS Lambda, AWS Secrets Manager, and AWS Systems Manager (SSM) Parameter Store — all deployed using the [AWS CDK](https://aws.amazon.com/cdk/).

It creates:

* ✅ A **Secrets Manager secret**
* ✅ An **SSM Parameter**
* ✅ A **Python Lambda** that reads both using `py-secrets-cache`

---

## Prerequisites

If you’re new to AWS/CDK, here’s what you’ll need:

1. **AWS Account** → [Sign up here](https://aws.amazon.com/free/) (the free tier is enough).
2. **AWS CLI** → [Install guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

   ```bash
   aws configure
   ```

   (set your access key, secret key, default region).
3. **CDK Toolkit**

   ```bash
   npm install -g aws-cdk
   ```
4. **First-time setup (per account/region)**

   ```bash
   cdk bootstrap
   ```

---

## Getting Started

Clone this repo and set up a Python virtual environment:

```bash
git clone https://github.com/rnag/secrets-cache-cdk-example.git
cd secrets-cache-cdk-example

python3 -m venv .venv
source .venv/bin/activate   # (on Windows: .venv\Scripts\activate)

pip install -r requirements.txt
```

---

## Deploy the Stack

Synthesize and deploy with:

```bash
cdk synth
cdk deploy
```

This will:

* Deploy the stack
* Show you the Lambda’s outputs in the terminal

---

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
