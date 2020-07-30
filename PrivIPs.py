import subprocess 
import re 

bad_chars = [',','[', ']', '(', ')', '\n', ' '] 
regions = ["ap-northeast-1", "ap-northeast-2", "ap-south-1", "ap-southeast-1", "ap-southeast-2", "ca-central-1", "eu-central-1", "eu-north-1", "eu-west-1", "eu-west-2", "eu-west-3", "sa-east-1", "us-east-1", "us-east-2", "us-west-1", "us-west-2"] 

for region in regions: 
	print region 
	process = subprocess.Popen(["aws", "--region", region, "ec2", "describe-instances", "--query", "Reservations[].Instances[][PrivateIpAddress]"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True) 
	output = process.communicate() 
	for i in bad_chars : 
		output = ''.join(output).replace(i, '') 
	if output and output.strip(): 
		output = output.strip('|') 
		output = output.strip('\t')
		output = output.strip('null')
		output = output.replace('null', '')
		print output.strip()
