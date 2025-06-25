# ARX Service Startup Guide

## Overview

This guide provides detailed instructions on how to start the ARX Service without setting the system JAVA_HOME. The deliver folder contains a complete Java Runtime Environment, eliminating the need for additional Java installation.

## Requirements

- Windows operating system
- Extracted deliver folder
- No Java installation required (JRE 17 is bundled)

## Startup Methods

### Method 1: Using Startup Script (Recommended)

**Steps:**
1. Navigate to the deliver folder
2. Double-click the `start.bat` file
3. Wait for the service to start

**Command Line:**
```bash
cd deliver
start.bat
```

**Advantages:**
- Simplest and most reliable
- Automatically configures environment variables
- No manual setup required

### Method 2: Direct Java Path Specification

**Steps:**
1. Open Command Prompt
2. Navigate to the deliver folder
3. Execute the following command:

```bash
cd deliver
jre\bin\java -jar arx-service-1.0.0.jar --server.port=8080
```

**Advantages:**
- Most direct approach
- No dependency on environment variable settings
- Full control over startup parameters

## Service Verification

### 1. Check Console Output

After successful startup, you should see output similar to:
```
  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::                (v2.x.x)

2023-xx-xx xx:xx:xx.xxx  INFO 1234 --- [           main] c.a.s.ArxServiceApplication              : Starting ArxServiceApplication...
2023-xx-xx xx:xx:xx.xxx  INFO 1234 --- [           main] c.a.s.ArxServiceApplication              : Started ArxServiceApplication in x.xxx seconds
```

### 2. Access Health Check Endpoint

Visit in browser: `http://localhost:8080/api/health`

Should return JSON response similar to:
```json
{
  "service": "arx-service",
  "status": "UP",
  "timestamp": "2023-xx-xxTxx:xx:xx.xxx"
}
```

### 3. Access Hello Endpoint

Visit in browser: `http://localhost:8080/api/hello`

Should return JSON response similar to:
```json
{
  "message": "Hello from ARX Service!",
  "status": "success",
  "timestamp": "2023-xx-xxTxx:xx:xx.xxx"
}
```

## Port Configuration

### Change Default Port

**Method 1: Modify Startup Script**
Edit the `start.bat` file and change the last line to:
```bash
java -jar arx-service-1.0.0.jar --server.port=9090
```

**Method 2: Specify Port During Startup**
```bash
jre\bin\java -jar arx-service-1.0.0.jar --server.port=9090
```

### Common Port Examples

- 8080: Default port
- 9090: Alternative port
- 8081: Development environment port

## Troubleshooting

### Issue 1: Port Already in Use

**Error Message:**
```
Web server failed to start. Port 8080 was already in use.
```

**Solution:**
1. Find the process using the port:
   ```bash
   netstat -ano | findstr :8080
   ```
2. Terminate the occupying process or change the port

### Issue 2: Java Version Incompatibility

**Error Message:**
```
UnsupportedClassVersionError
```

**Solution:**
- Ensure you're using the JRE from the deliver folder
- Do not use system-installed Java

### Issue 3: Insufficient Permissions

**Error Message:**
```
Access is denied
```

**Solution:**
1. Run Command Prompt as Administrator
2. Check folder permissions

### Issue 4: Insufficient Memory

**Error Message:**
```
OutOfMemoryError
```

**Solution:**
Increase JVM memory parameters:
```bash
jre\bin\java -Xmx2g -jar arx-service-1.0.0.jar --server.port=8080
```

## Stop Service

### Method 1: Console Stop
Press `Ctrl + C` in the Command Prompt window running the service

### Method 2: Force Terminate Process
```bash
# Find process ID
netstat -ano | findstr :8080

# Terminate process (replace PID with actual process ID)
taskkill /PID <PID> /F
```

## Log Viewing

### Console Logs
Detailed log information will be displayed in the console during service startup

### Log Files
If log files are configured, they are typically located in:
- `logs/` directory
- Or current running directory

## Frequently Asked Questions

**Q: Why is Java installation not required?**
A: The `jre/` directory in the deliver folder contains a complete Java Runtime Environment that is self-contained and does not affect other applications on the system.

**Q: Can multiple instances be run simultaneously?**
A: Yes, but different ports must be used, for example:
```bash
# Instance 1
jre\bin\java -jar arx-service-1.0.0.jar --server.port=8080

# Instance 2
jre\bin\java -jar arx-service-1.0.0.jar --server.port=8081
```

**Q: How to set up auto-start on boot?**
A: You can add `start.bat` to Windows startup items or create a Windows service.

**Q: Which operating systems are supported?**
A: Current configuration is suitable for Windows systems. For other operating systems, please contact the delivery team.

## Support

For other issues, please contact the delivery team for technical support. 