<!--
title: 'AWS Serverless Alexa Skill for Lambda example in Python'
description: 'This example demonstrates how to setup your own Alexa skill using AWS Lambda.'
layout: Doc
framework: v1
platform: AWS
language: Python
authorLink: 'https://github.com/franczyk'
authorName: 'Gary Franczyk"
authorAvatar: 'https://avatars0.githubusercontent.com/u/425913?v=4&s=140'
-->
# Serverless Alexa Skill for Netflix Best of list

This code pulls a best-of list from collider.com for this month's best items on Netflix.  It outputs the content in a random order.

```bash
serverless deploy
```

The expected result should be similar to:

```bash
Serverless: Creating Stack...
Serverless: Checking Stack create progress...
Serverless: Stack create finished...
Serverless: Packaging service...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading service .zip file to S3 (2 KB)...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
Serverless: Stack update finished...

Service Information
service: aws-python-alexa-skill
stage: dev
region: us-east-1
api keys:
  None
endpoints:
  None
functions:
  aws-python-alexa-skill-dev-bestofnetflix: arn:aws:lambda:us-east-1:377024778620:function:aws-python-alexa-skill-dev-bestofnetflix
```

Next we need to setup a Alexa skill. Once you've signed up for the Amazon Developer Platform visit `https://developer.amazon.com/edw/home.html`. There you should see the following screen:

![Welcome](https://cloud.githubusercontent.com/assets/223045/21183285/8403b37c-c211e6-89c0-d36582010af8.png)

Next click on `Add a new Skill`:

![Add Skill](https://cloud.githubusercontent.com/assets/223045/21183286/840512c211e6-84945b6b45e83b.png)

Go through the steps and fill in all the required fields e.g. Intent Schema and Sample Utterances:

Intent Schema
```
{
  "intents": [
    {
      "intent": "best-of-netflix",
      "slots": [
        {
          "name": "UpperLimit",
          "type": "AMAZON.NUMBER"
        }
      ]
    }
  ]
}
```

Sample Utterances
```
best-of-netflix movies
best-of-netflix what are the best movies on netflix
```

Fill in the Lambda ARN which was printed or run `serverless info` to retrieve the ARN again.


Check out this [Amazon guide](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/overviews/steps-to-build-a-custom-skill#your-skill-is-published-now-what) to learn more about how to submit your skill for publication.
