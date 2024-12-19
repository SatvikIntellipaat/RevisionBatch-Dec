IAM Service
-----------

-Users: Can acces the aws account by 2 methods -Cli, - AWS console
-Groups: Collection of Users
-Roles: Temperoray access to a user and give access to services
-Policies: Permissions
----> aws-polcy: EC2:fullaccess
----> custom-policy:
----> to create an s3 buket or to create an ec2 machine

---------------
EC2-machine (view:describe) 
 Name --- satvik-ec2 ----->
            {
                key:"Name",
                Value: "satvik-ec2"
            }
--tags(createtag)
--ami/image (describeimage)
--instancetype(describeinstncetype)
--keypair(describekeypair,createkeypair)
---vpc(describevpc)
---subnet(descibesubnet)
---sg(createsg,describesg)
---storage(ebs volumes)(describevolume,createvolume,attachvolume)
---network-interface(createnetworkinterface,attachednetworkinterface)
--run instance permission
---view the instances: describeinstances

------------------------------------------------------------------------------------------------------------------------
HomeWork: create a policy for a cli user: he can only get object,upload object into a specific s3 bucket (name-homework)
--> that he cant delete any object name having a prefix: Satvik
(ex:satvikhello.txt ,hello.txt-->cant delete)
support@intellipaat.com ---> Subject: Satvik-iam-revission-assignment
------------------------------------------------------------------------------------------------------------------------
Answer: Policy
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "Fullacceforallobjects",
			"Effect": "Allow",
			"Action": [
				"s3:PutObject",
				"s3:GetObject",
				"s3:DeleteObject"
			],
			"Resource": "arn:aws:s3:::satvik-81124/*"
		},
		{
			"Sid": "denydeletepermissionforobjectcontainingsatvikinstarting",
			"Effect": "Deny",
			"Action": [
				"s3:DeleteObject"
			],
			"Resource": "arn:aws:s3:::satvik-81124/Satvik*"
		}
	]
}

EC2
----------------------------------------------------------------
--> Computing services---> network,memory,storage....
instancetype:memory(ram),cpu
----------------------------
--> GeneralPurpose: Daily purpose (balanced)
    -->t-series ex:t2.micro (cost-effect)
    -->m-series (consitent perfomance)
--> Compute Optimized:  High perfomance Proceccors
    --> c-series (batch processing)
--> Memory Optimized (highly used for memory intensed tasks)
    --> r-series
    --> x-series
--> Accerlerate computing (ml)(gpus)
    --> p-series
    --> g-series (grahics)
--> Storage Optimized (high iops)
    --> i-series
    --> d-series

Tenancy Models:(deploying the resource)
----------------------------
1.Shared Tenancy : The underlying hardware can be shared other coustomres (cost-effeciect)
2.Dedicated Instance: physical server will be completely giving you.(hardware: aws manages)
3.Dedicated Hosts:(hardware: you manage)

Instance Offerings:(Buy)
-----------------------------
1.On-Demand Instance: (dont have any commitemt)
2.Reserved Instance: (commit to 1-3 years)
3.Savings Plan:(similar to reserved instance but commit a price [3-years for $100/hr])
4.Spot Instance(bidding for the instance)(not reliable, cheap)
5.Dedicated Hosts (BYOL)
6.Capacity Reserveraions

Q. What service you will be using for the photo processing company. The coustomers can wait for the prints since the 
companies processing algoruitum is great.For cost optimizing
A. Spot Instnance ---Answer(cheap)
B. Reserved Instance
C. SQS Queue -- one option
D. On-Demand Instance

------------------------------------------------------------------------------------------
EBS(Elastic block storage)---> hard disk
(Storage)
Disadvantages:
--->1. Both ec2 and ebs volume should be in same Az
--->2. Multi Attach cont possible 

Advantages:
--->1. Low Latency

(Multi-attach--> 15 instances(AMi---nitro based) Ebs--io1,io2 )
https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes-multi.html

----------------------------------------------------------------------------
Volumes Types:
1. ssd(high perfomance)
--> gp3
--> gp2
--> io1
--> io2
2. hdd(archieve data)
--> st1
--> sc1

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Day-3
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

EBS-Block storage
--> is in unformatted state(i.e ebs volume is not compatable with ec2 use--> it is not in ready state)
To use ebs volume:
1. Create an ebs volume in the same az of your ec2 machine
2. Attach the volume to the ec2 machine(physicall)
3. Format the ebs(making the ebs volume in usable state--> format with an filesystems(ext4,xfs))
4. Mount the ebs

####Commands#####
df -h ---> stroage space which can be used by os (-h human readable form)
lsblk ---> list of block storage which are attached to ur ec2 machine
mkfs -t FILE-SYSTEM DEVICENAME (ex: mkfs -t ext4 /dev/xvdb)
mkdir storage
mount DEVICDENAME FOLDERNAME (ex: mount /dev/xvdb storage)

Note: 
1.IF you store some data in another vokume of your ec2, and detach it.Later attached to another ec2 machine, then the data will still be available.
2.You can detach the root volume, but if you start the ec2 it will stop working.

Volume: delete when instnce deleted (Delete on termination) -- enable (default enabled on root volume)

------------------------------------------------------------------------------------------------------------------------
HomeWork:1. You will be adding additional volume to an ec2 machine and store some date inside it, then detach it and mount to another machine and check that file is there or not.
2. Detach your root volume and run the machine.
------------------------------------------------------------------------------------------------------------------------


CLI
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
https://docs.aws.amazon.com/cli/latest/userguide/cli_acm_code_examples.html

aws configure--accesskey,secreetaccesskey

Thursday-explanation
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
ebs--backup: snaphot(region)---> Copy can be done to other regions as well
1. Snaphots are incremental: This means after the initial snapshot is done, subseqeunt snaphots only store the changes that have taken place since the previous snaphot
a file -- hello  --> 1st snaphot (hello)
a file -- hello world ---> 2 nd snaphot(1st snaphot + world)

AMI/Image: backup of your ec2-machine:

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Day-4
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
AMI:
1.Can be Multiple regions
2.AMI contains only software configuration files
3.AMI contains snapshot of root volume

Key-pair : authenticate

q. I Dont have a key-pair file (private file got deleted). Now i want to give access to my firend(without dasboard access) for my ec2. What are the ways i can connect to the ec2 machine?
1. Creatin an ami and launching a new machine
2. i can detach the volume and add to new machine 
3. instnace connect --> without key pair (not in this scenario)
4. (ssh user) and password (hw---> linux sesson)
5. puttyzen --> create a public and private key (new).  Copy the public key into the auhorized keys
------------------------------------------------------------------------------------------------------------------------------------------------------
ssh -i keypair.pem ubuntu@ip
ssh ubuntu@ip ---> enter --> passowrd:*****
-------------------------------------------------------------------------------------------------------------------------------------------------

loadbalancer
--------------
To distribute load betwen the servers

Types of load-balancers
----------------------
1. Application LB (v2) -->  Classic Load Balancer (V1)
2. Network LB (v2)
3. Gateway LB (v2)

ALB
---
1. It will be working on http and https
2. Application layer od osi model
3. Web requests
4. Path-based routing on alb (url ---> www.amazon.com/home  , www.amazon.com/payments)
5. Web servers

ALB vs CLB
----------
1. On appliation & transpot layer of osi model
2. alb is intelligent.
3. alb --> target group, clb --> targets

alb is alnalyzing url path,url-headers, slow when we compare with nlb

NLB
-----
1. Transport layer of the osi model
2. tcp and udp protocol
3. http --> tcp : 80 : no---> url works on application layer
4. server to server

GLB
-----
1. network layer and transport layer of osi model
2. routes the traffic based on ip address
3. Geneve protocol
4. when you want 3rd party services

------------------------------------------------------------------------------------------------------
Scalling:
1. Horizantal-scaling:
You increase or decrease the number of machine of same capacity ex: 1cpu machine  -->  2 of 1cpu machine
2. vertical-scaling:
You increase or decesare the capacity of reesource ex: 1cpu machine -> 2cpu machine

asg--> horizantal
vertical scaling --<instance type>
------------------------------------------------------------------------------------------------------
Types of scalling polices
1. simple --> add,delete,set (quantity,target)
2. target --> (target--> average)
3. step --> we can scaling in step wise (1-60%,3- 70%,5- 80%)
4. predictive --> machine learning algo to analyze previous patters in the monitoring data and do predication for futue
5. scheduling --> based on the schduled event it will scall up (ex: everyday at 12 noon launch 4 machines)

------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------
Day-5
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Route 53
-------
DNS Works on port 53
DNS service by AWS --> It translates domain name to an Ip address

Hosted Zone
----------
Conatiner for DNS records

Types of Records
------------------
A --> to tanstlate a domain to ipv4 address/ subdomain to an ipv4 / subdomain to aws services dns (Address Record)
AAA ---> to translate a domain to ipv6
ns record ---> nameserver record
CNAME  ---> it is a type of alias record | to route the traffic between a subdomain to an another domain
mx record ---> mailserver
txt record ---> to confirm the authenticity of mails

ex : Intellipaat.com ---> root domain
	lms.Intellipaat.com ---> sub-domain

Routing Policy
--------------
1. Simple Routing ---> Maps a single domain/subdomain to one resource
2. Weighted Routing --> Distribute the traffic across different resources based on the weight
3. Geo-Location Routing --> Routes traffic based on location of user
4. Geo-Proximity Routing --> It consider the geographic distance between the user and resource
5. Failover Routing --> Routes the traffic to the primary server, but if primary fails then it routes to the backup server
-----------------------------
Q. You are deploying anew version of our app and want 90% of traffic to go the stable version and 10% to the new version for testing. Which routing policy shpuld you use?
Answer: Weighted Routing

Conifg:
Ubuntu Server-1:
-----------------
#!/bin/bash

sudo su
apt install apache2 -y
echo "<h1>Server-1</h1>" > /var/www/html/index.html
----------------------------------------------------
http://ip address --> Server-1

----------------------------------------------------
----------------------------------------------------
Ubuntu Server-2: 
---------------
#!/bin/bash

sudo su
apt install apache2 -y
echo "<h1>Server-2</h1>" > /var/www/html/index.html
mkdir -p /var/www/html/payments       ----> to create a folder named payments in html folder
echo "<h1>Welcome to payments page</h1>" > /var/www/html/payments/index.html
---------------------------------------------------------------------------
http://ip-adress  --> Server-2
http://ip-adress/payments ---> welcome to payments page

cross-zone LB