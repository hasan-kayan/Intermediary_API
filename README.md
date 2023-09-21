# Intermediary_API

That is a very simple midle point for a specific purpose, as we know AWS S3 service is able to keep abjects and most of our systems are connected to this S3 system. 
In some ready-made static site generaters are forcing us to use their own systems and dont allows us to connect directly to our systems, at this state mostly they are able to throw packages to specific addresses. 
In this case we have to catch these packages and insert them into our S3 bucket, and here is a simple script for this. 

## How to use? 

First of all you need to create a S3 Bucket and a policy according to this bucket and than you need to create a user due to your policy. These steps are essential because of security concerns. 
After these steps you can check your accsess ID and accsess key for script and enter them after these steps you can deploy this anywhere you want. 

