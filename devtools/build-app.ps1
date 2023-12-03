#IMPORTANT: This script must be run in the VSCode via the integrated terminal

#Required Enviornmental Variable:
#PYTHONPATH: [path to repository on the file system]
#ex. value: C:\git-repos\virtual-graphing-calculator-repo\development\mvgcalc

Write-Host "*********************************************************************************"
Write-Host "*"
Write-Host "*                     BEGIN MVGCALC DEPLOYMENT"
Write-Host "*"
Write-Host "*********************************************************************************"

$projectRoot = [System.Environment]::GetEnvironmentVariable('PYTHONPATH')

#check if required environmental variables exist
if (!$projectRoot) {
    Write-Host "PYTHONPATH environmental variable is missing." 
    Write-Host "PYTHONPATH environmental variable must be added." 
    Write-Host "exiting script..."  
    exit  
}

#delete existing build folders
$distDirDest = "$projectRoot/deployment/dist"
$buildDirDest = "$projectRoot/deployment/build"

$paths = $distDirDest, $buildDirDest
$pathsExist = ($paths | Test-Path) -notcontains $false

if ($pathsExist) {
    Remove-Item -Path $distDirDest -Recurse
    Write-Host "Directory $distDirDest deleted successfully."
    Remove-Item -Path $buildDirDest -Recurse
    Write-Host "Directory $buildDirDest deleted successfully."
}

$virtEnvScriptPath = "$projectRoot\.venv\Scripts"

#if python virtual environment not active then activate virtual environment
if (!$env:VIRTUAL_ENV) {

    Write-Host "No python virtual environment is currently active."

    Write-Host "Activating python virtual environment..."
    $activateScriptFileName = "Activate.ps1"
    $activateVirtEnvPath = "$virtEnvScriptPath\$activateScriptFileName"
    Invoke-Expression $activateVirtEnvPath
    
    # check if Activate.ps1 was sucessfully executed
    if ($LastExitCode -eq 0) {
        Write-Host "Python virtual environment activated."
    } else {
        Write-Host "Error: Script execution failed with exit code $LastExitCode."
        exit
    }
    
    Write-Host "******************************BUILD TERMINATED******************************"
    Write-Host "Re-Execute build-app.ps1."
    Write-Host "exiting."
    exit
}

$deploymentDir = "$projectRoot\deployment"

#deploy MVGCalc
Write-Host "Start MVGCalc delployment."
Start-Process -Wait pyinstaller "$deploymentDir\config\main.spec"

#validate build
$distDirSource = "$projectRoot\devtools\dist"
$buildDirSource = "$projectRoot\devtools\build"

$paths = $distDirSource, $buildDirSource
$pathsExist = ($paths | Test-Path) -notcontains $false
if ($pathsExist) {

    
    Move-Item -Path $distDirSource -Destination $distDirDest
    Write-Host "Moved $distDirSource to $distDirDest."
    Move-Item -Path $buildDirSource -Destination $buildDirDest
    Write-Host "Moved $buildDirSource to $buildDirDest."

    $mvgCalcExePath = "$distDirDest\MVGCalc.exe"

    if (Test-Path -Path $mvgCalcExePath) {
        
        Write-Host "*********************************************************************************"
        Write-Host "*                     MVGCALC DEPLOYMENT SUCCESS"
        Write-Host "*********************************************************************************"

    } else {
        
        Write-Host "*********************************************************************************"
        Write-Host "*                     NO EXE - MVGCALC DEPLOYMENT FAILED"
        Write-Host "*********************************************************************************"
    }

    Write-Host "*********************************************************************************"
    Write-Host "*"
    Write-Host "*                     END MVGCALC DEPLOYMENT"
    Write-Host "*"
    Write-Host "*********************************************************************************"

}




