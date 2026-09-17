Incident Response Guide



This guide covers common issues encountered while deploying and running this project, their likely causes, and how to resolve them.



1\. Deployment fails: Azure quota exceeded



Symptom: `az appservice plan create` fails with "Operation cannot be completed without additional quota."



\*\*Cause:\*\* New Azure subscriptions often start with zero quota for certain VM sizes in certain regions.



Resolution:

\- Try creating the resource in a different region (e.g., westus2, centralus, westeurope)

\- If the issue persists across regions, request a quota increase via the Azure Portal (Quotas blade)



2\. Azure CLI login crashes with a tenant error



Symptom: `az login` fails with `AttributeError: 'NoneType' object has no attribute 'get'`



Cause: A known Azure CLI bug when it cannot automatically select a tenant.



Resolution:

\- Run `az logout` and `az account clear` to reset the session

\- Find your Tenant ID in Microsoft Entra ID in the Azure Portal

\- Log in again with `az login --tenant YOUR-TENANT-ID`



3\. CI pipeline fails at the flake8 step



Symptom: GitHub Actions fails with "Process completed with exit code 1" on the lint step.



Cause: Code style violations — commonly spacing, line length, or missing/extra newline at end of file.



Resolution:

\- Scroll up in the failed step's log to see the specific flake8 errors (e.g., E302, E501, W292, W391)

\- Fix formatting locally, then verify with `python -m flake8 app.py --max-line-length=100` before pushing

\- For newline issues specifically, verify file bytes in PowerShell: `\[System.IO.File]::ReadAllBytes("$PWD\\app.py")`



4\. Resource creation blocked by Azure Policy



Symptom: `RequestDisallowedByPolicy` error mentioning "Require a tag on resource groups."



Cause: The subscription enforces a policy requiring specific tags (e.g., `Environment`) on all resource groups.



Resolution:

\- Read the `evaluatedExpressions` section of the error to find the exact required tag key

\- Add the tag when creating the resource, e.g. `--tags Environment=Development`



5\. App becomes unresponsive in production



Symptom: The live app stops responding or shows an error page.



Cause: Could be an application crash, a bad deployment, or a resource limit issue.



Resolution:

\- Check `/health` endpoint manually — if it fails, Azure's Auto-Heal should restart the app automatically

\- Check the Log Stream in the Azure Portal for recent error messages

\- Check the Metrics blade for CPU/memory spikes

\- If needed, manually restart with: `az webapp restart --name devops-project-webapp123 --resource-group devops-project-rg`

