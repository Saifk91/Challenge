# Challenge Answer 1-
The diagram shows a simple 3- tier architecture that can be deployed on Azure or any cloud Vendor.
1)  There are 2 Windows Virtual machines.
2) VM balanced by Load balancers
3) 2 Linux VMs
4) SQL database with failover configured.

The deployment can be done on Azure using the GUI, once a VM is deployed then we can use its template to duplicate the same (or by CLI as well).
For example create W1 as required, and then fetch its template do deploy W2 (with some tweaks like address space, name, region, disk etc. as needed)
Similar process for Linux.
VMs can be put in availability set / availability zones to increase HA.
The SQL database will have a failover policy (Geo-replication) as well in case of any issues. Create a failover policy for automatic shift, and use that failover group name to connect to the database. Therefore maintaining 99.95% of SLA.
Also in terms of reproducibility, once all the resources are in place, one can download (or save in shared workspace)the Resource group template, using which the whole environment can be replicated whenever needed.
The VMs can also be used with recovery service vault to backup the data and restore when needed.
The resource group should have a Lock as well to prevent any unwarranted deletion.
Apart from these the Azure DevOps could be used here for commit and deployment of code.
Storage account: to store logs and diagnostics, or snaps if needed.
NSGs: to control access and ports
Monitoring and alerts for proactive monitoring.
Automation account: to start stop or copy the resources wherever needed.
We can also keep the VMs in scale sets to burst and shrink as per memory or CPU utilization, and the same set can be mapped to LBs.

Please refer the architectural diagram above.

Also i have written and attached a sample to deploy resources in AWS using terraform.

