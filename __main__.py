"""A Google Cloud Python Pulumi program"""

import pulumi
import os
import configparser

from pulumi_gcp import storage

# Get Environment set Variables to read Config.ini
#pulumi_config = pulumi.Config
#pulumi_env = pulumi_config.require('env')
#print(pulumi_env)
SET_ENV = 'dev'

#Set Project Name from config file
PROJECT_NAME = 'joshua_martin_mgsandpit1'

#Set Location for GCP from Config file
LOCATION = 'US'

# Create a GCP resource (Storage Bucket)
bucket = storage.Bucket(
    f'static_page_{PROJECT_NAME}', 
    location=LOCATION,
    name='testjoshsandpit.com',
    website= storage.BucketWebsiteArgs(
        main_page_suffix='index.html',
        not_found_page='404.html'
    ),
    cors= [storage.BucketCorArgs(
            origins=["https://testjoshsandpit.com"],
        methods=[
            "GET"
        ],
        response_headers=["*"],
        max_age_seconds=3600,
    )]
    )

# Export the DNS name of the bucket
pulumi.export('bucket_name', bucket.url)
pulumi.export('bucket_cors',bucket.cors)
pulumi.export('bucket_ecryption',bucket.encryption)
