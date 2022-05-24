aws ecr get-login-password --region eu-central-1| docker login --username AWS --password-stdin 254701324686.dkr.ecr.eu-central-1.amazonaws.com
docker build -t data-pipeline -f DockerfileAWSLambda .
docker tag data-pipeline 254701324686.dkr.ecr.eu-central-1.amazonaws.com/test-lambda
docker push 254701324686.dkr.ecr.eu-central-1.amazonaws.com/test-lambda


# update lambda functions
aws lambda update-function-code --function-name test-lambda --image-uri 254701324686.dkr.ecr.eu-central-1.amazonaws.com/test-lambda:latest
