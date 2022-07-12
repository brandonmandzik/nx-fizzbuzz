

# NxFizzbuzz

This project was generated using [Nx](https://nx.dev).

<p style="text-align: center;"><img src="https://raw.githubusercontent.com/nrwl/nx/master/images/nx-logo.png" width="450"></p>

🔎 **Smart, Fast and Extensible Build System**

# Introduction

Fizzbuzz is a small HTTPS game backed by the Amazon AWS cloud infrastructure. The game is simply playable by calling an HTTPS API-Endpoint with a provisioned number. Based on the request, the API reponds with either the words "Fizz", "Buzz" or "Fizzbuzz". The logic behind the game is pretty simple and can be summerized with three rules:
  1. If the number is divideable by 3 -> Return "Fizz"
  2. If the number is divideable by 5 -> Return "Buzz"
  3. If the number is divideable by 3 AND 5 -> Return "Fizzbuzz"

Technically the game is build on top of the following AWS technologies: 
- AWS Lambda: For provisioning a serverless solution for the handler function (logic/backend)
- AWS API Gateway: For proxying a RESTful https endpoint to the public internet for the lambda function 
- AWS IAM & Cognito: To block public and unauthorized access to the game
- AWS CDK & Cloudformation: for providing the infrastracture as code in order to have automated fallbacks and roll-outs


# Requirements
- AWS CLI 2.5.4
- Python 3.9
- pytest
- Nx 14.4.0
- CDK 2.28.0
- VCS (Git & Github)

# Getting started
First make sure to have all named requirements installed/prepared in order to have a sucessfull development enviroments. Each of them is necessary to run the build, test and deploy commands which are also included in an automated CI/CD manner. In the following you will find the recommended installtions for Mac OS

1. AWS CLI
```
$ curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
$ sudo installer -pkg AWSCLIV2.pkg -target /
```

2. NX by nrwl
```
$ npm install -g nx
```

3. CDK
```
npm install -g aws-cdk
```

## Project Structure
<img width="153" alt="image" src="https://user-images.githubusercontent.com/35039517/178467958-f2efc336-9882-43e4-b1fa-ebbf3132533a.png">
Due to the fact that Nx is a tool for managing projects and repositories, it makes it easier to handle mutiple projects in a single repository (Monorepo) as you can customize and wrap all project/application relevant commands into simpler global NX commands.

<br>The most important folders here are: `.github, packages, and nx.json` at the root level for defining the repositories scope. The `packages` folder holds the individual applications and libraryies we want to manage. In this case we have the Lambda application (`packages/fizzbuzz`) and the AWS CDK application (`packages/infrastructure`) for synthesizing our CloudFormation templates. 

<br>It's good to know that an application needs to hold a `project.json or package.json` (when living in an JS enviroments) at the directories root level in order to recognize it as an indiviual application. Further more the `.json` definition hold relevant information about how to wrap the app into the NX enviroment.

<br>NX allows you to create and handle any application you want inside. In case you need additional libraries or similar you can create the projects inside of `packages` and in parrallel the necessary `project.json`. You can use any desired language or framework. The language specific commands can then be wrapped into NX commands. Just make sure to have satisfied dependecies on this.

### Example and Use-Case of project.json
In this case we use the application `packages/fizzbuzz` which is our lambda function handler written in python. Python has a native testing solution with the pytest library. Usally you would test it by running the python specific commands in your terminal. Since NX is our global project manager we can wrap these into NX run commands.  
```
{
  "root": "packages/fizzbuzz",
  "sourceRoot": "packages/fizzbuzz/src",
  "projectType": "application",
  "targets": {
    "test": {
      "executor": "nx:run-commands",
      "options": {
        "command": "python3 -m pytest -v",
        "cwd": "packages/fizzbuzz/src"
      }
    },
    ...
}   
```
This json document tells NX how to handled the application related commands. Targets in this case are the nx run-commands for the specific application. E.g. `test` is defined and tells it what to do underneath. See the following:
```
// python native command
$ python3 -m pytest -v 
// resolves into
$ nx run fizzbuzz:test
```

You can specify custom targets you want, for any desired application or library. NX is here to globally handle all staging process for all applications living inside of the monorepo. It helps by having a common syntax for all apps. 


# Build
Due to the fact that the solution is provisioned by a serverless infrastructure there are no specific build processes. AWS Lambda is a serverless FaaS (function) and can be populated with many different languages. In our case we have the scripting language Python. It will be directly interpreted from the source code and don't need any compilation or executable. So in a deeper Sense building our Lambda functions means zipping it as we follow the zip-it-ship-it ideology by amazon. Further more to this topic comes in the deploy part.

When it comes to the infrastructure we indeed need to build the CloudFormation template this time before deploying it. AWS CDK firstly need to build the Template which will be deployed to an account and region. Based on that template guidance, AWS can then build the infrastracture stack. 
To do so run the following: `$ nx run infrastrucuture:bootstrap`

# Deploy
One of the Lambda deploying techniques is called zip-it-ship-it. Do so, you simply need to compress the src directory you want to deploy into a zip directory and upload it through the AWS CLI to the desired Lambda function. You can do so by running `$ nx run fizzbuzz:deploy` underneath NX doing the things that have been described before.

For the infrastructure, when the bootstrapping process is completed you need to run `$ nx run infrastructure:deploy`

# Test

In order to test the handler function you can either do it manually by creating testing events inside of the AWS management console or by running pytest. The second option is wrapped into a NX run command: `$ nx run fizzbuzz:test`

```
> nx run fizzbuzz:test

============================= test session starts ==============================
platform darwin -- Python 3.8.13, pytest-7.1.2, pluggy-1.0.0 -- /opt/homebrew/opt/python@3.8/bin/python3.8
cachedir: .pytest_cache
rootdir: /Users/b.mandzik/Documents/Codespace/nx-fizzbuzz/packages/fizzbuzz/src
collecting ... collected 5 items

test_lambda_function.py::test_validateInput_zero PASSED                  [ 20%]
test_lambda_function.py::test_validateInput_wrongNumber PASSED           [ 40%]
test_lambda_function.py::test_validateInput_fizz PASSED                  [ 60%]
test_lambda_function.py::test_validateInput_buzz PASSED                  [ 80%]
test_lambda_function.py::test_validateInput_fizzbuzz PASSED              [100%]

============================== 5 passed in 0.00s ===============================

 ———————————————————————————————————————————————————————————————————————————————————————————————————————

 >  NX   Successfully ran target test for project fizzbuzz (297ms) 
```

# FAQ

### How to I create additionally applications?
### Are there any CI/CD pipelines?
### How do I authorizes the usage?

# Appendix

### CDK Docu
[Click me](https://docs.aws.amazon.com/cdk/api/v2/)

### Lambda Python Docu
[Click me](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html)

### Nx Documentation
[Click me](https://nx.dev/getting-started/intro)
