#!/usr/bin/python
'''
Copyright 2018 nugatorium

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

https://github.com/nugatorium/ami_bios_codes
'''

import json
import sys

jsonData = '''{
  "6A":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"North Bridge DXE SMM initialization is started",
    "type":"Progress"
  },
  "6B":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"North Bridge DXE initialization (North Bridge module specific)",
    "type":"Progress"
  },
  "F3":{
    "phase":"PEI Phase",
    "checkpoint":"Recovery (PEI)",
    "message":"Recovery firmware image is loaded",
    "type":"Progress"
  },
  "F4":{
    "phase":"PEI Phase",
    "checkpoint":"Recovery (PEI)",
    "message":"Reserved for future AMI progress codes",
    "type":"Progress"
  },
  "6E":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"North Bridge DXE initialization (North Bridge module specific)",
    "type":"Progress"
  },
  "F6":{
    "phase":"PEI Phase",
    "checkpoint":"Recovery (PEI)",
    "message":"Reserved for future AMI progress codes",
    "type":"Progress"
  },
  "DD":{
    "phase":"DXE Phase",
    "checkpoint":"DXE errors",
    "message":"DXE phase BMC self-test failure",
    "type":"Error"
  },
  "3C":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"Post-Memory North Bridge initialization (South Bridge module specific)",
    "type":"Progress"
  },
  "3B":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"Post-Memory South Bridge initialization is started",
    "type":"Progress"
  },
  "3A":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"Post-Memory North Bridge initialization (North Bridge module specific)",
    "type":"Progress"
  },
  "3F":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"OEM post memory initialization codes",
    "type":"Progress"
  },
  "3E":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"Post-Memory North Bridge initialization (South Bridge module specific)",
    "type":"Progress"
  },
  "3D":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"Post-Memory North Bridge initialization (South Bridge module specific)",
    "type":"Progress"
  },
  "02":{
    "phase":"SEC Phase",
    "checkpoint":"SEC Execution",
    "message":"AP initialization before microcode loading",
    "type":"Progress"
  },
  "03":{
    "phase":"SEC Phase",
    "checkpoint":"SEC Execution",
    "message":"North Bridge initialization before microcode loading",
    "type":"Progress"
  },
  "00":{
    "phase":"SEC Phase",
    "checkpoint":"SEC Execution",
    "message":"Not Used",
    "type":"Not Used"
  },
  "01":{
    "phase":"SEC Phase",
    "checkpoint":"SEC Execution",
    "message":"Power on. Reset type detection (soft/hard)",
    "type":"Progress"
  },
  "06":{
    "phase":"SEC Phase",
    "checkpoint":"SEC Execution",
    "message":"Microcode loading",
    "type":"Progress"
  },
  "07":{
    "phase":"SEC Phase",
    "checkpoint":"SEC Execution",
    "message":"AP initialization after microcode loading",
    "type":"Progress"
  },
  "04":{
    "phase":"SEC Phase",
    "checkpoint":"SEC Execution",
    "message":"South Bridge initialization before microcode loading",
    "type":"Progress"
  },
  "05":{
    "phase":"SEC Phase",
    "checkpoint":"SEC Execution",
    "message":"OEM initialization before microcode loading",
    "type":"Progress"
  },
  "08":{
    "phase":"SEC Phase",
    "checkpoint":"SEC Execution",
    "message":"North Bridge initialization after microcode loading",
    "type":"Progress"
  },
  "09":{
    "phase":"SEC Phase",
    "checkpoint":"SEC Execution",
    "message":"South Bridge initialization after microcode loading",
    "type":"Progress"
  },
  "0B":{
    "phase":"SEC Phase",
    "checkpoint":"SEC Execution",
    "message":"Cache initialization",
    "type":"Progress"
  },
  "0C":{
    "phase":"SEC Phase",
    "checkpoint":"SEC Errors",
    "message":"Reserved for future AMI SEC error codes",
    "type":"Error"
  },
  "0A":{
    "phase":"SEC Phase",
    "checkpoint":"SEC Execution",
    "message":"OEM initialization after microcode loading",
    "type":"Progress"
  },
  "0F":{
    "phase":"SEC Phase",
    "checkpoint":"SEC Errors",
    "message":"Microcode not loaded",
    "type":"Error"
  },
  "0D":{
    "phase":"SEC Phase",
    "checkpoint":"SEC Errors",
    "message":"Reserved for future AMI SEC error codes",
    "type":"Error"
  },
  "0E":{
    "phase":"SEC Phase",
    "checkpoint":"SEC Errors",
    "message":"Microcode not found",
    "type":"Error"
  },
  "39":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"Post-Memory North Bridge initialization (North Bridge module specific)",
    "type":"Progress"
  },
  "38":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"Post-Memory North Bridge initialization (North Bridge module specific)",
    "type":"Progress"
  },
  "33":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"CPU post-memory initialization. Cache initialization",
    "type":"Progress"
  },
  "32":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"CPU post-memory initialization is started",
    "type":"Progress"
  },
  "31":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"Memory Installed",
    "type":"Progress"
  },
  "30":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"Reserved for ASL",
    "type":"Progress"
  },
  "37":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"Post-Memory North Bridge initialization is started",
    "type":"Progress"
  },
  "36":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"CPU post-memory initialization. System Management Mode (SMM) initialization",
    "type":"Progress"
  },
  "35":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"CPU post-memory initialization. Boot Strap Processor (BSP) selection",
    "type":"Progress"
  },
  "34":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"CPU post-memory initialization. Application Processor(s) (AP) initialization",
    "type":"Progress"
  },
  "60":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"DXE Core is started",
    "type":"Progress"
  },
  "FA":{
    "phase":"PEI Phase",
    "checkpoint":"Recovery Errors (PEI)",
    "message":"Invalid recovery capsule",
    "type":"Error"
  },
  "FB":{
    "phase":"PEI Phase",
    "checkpoint":"Recovery Errors (PEI)",
    "message":"Reserved for future AMI error codes",
    "type":"Error"
  },
  "FC":{
    "phase":"PEI Phase",
    "checkpoint":"Recovery Errors (PEI)",
    "message":"Reserved for future AMI error codes",
    "type":"Error"
  },
  "64":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"CPU DXE initialization (CPU module specific)",
    "type":"Progress"
  },
  "FE":{
    "phase":"PEI Phase",
    "checkpoint":"Recovery Errors (PEI)",
    "message":"Reserved for future AMI error codes",
    "type":"Error"
  },
  "FF":{
    "phase":"PEI Phase",
    "checkpoint":"Recovery Errors (PEI)",
    "message":"Reserved for future AMI error codes",
    "type":"Error"
  },
  "67":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"CPU DXE initialization (CPU module specific)",
    "type":"Progress"
  },
  "68":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"PCI host bridge initialization",
    "type":"Progress"
  },
  "69":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"North Bridge DXE initialization is started",
    "type":"Progress"
  },
  "9A":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"USB initialization is started",
    "type":"Progress"
  },
  "9C":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"USB Detect",
    "type":"Progress"
  },
  "9B":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"USB Reset",
    "type":"Progress"
  },
  "9E":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"Reserved for future AMI codes",
    "type":"Progress"
  },
  "9D":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"USB Enable",
    "type":"Progress"
  },
  "9F":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"Reserved for future AMI codes",
    "type":"Progress"
  },
  "C9":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"OEM BDS initialization codes",
    "type":"Progress"
  },
  "C8":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"OEM BDS initialization codes",
    "type":"Progress"
  },
  "C3":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"OEM BDS initialization codes",
    "type":"Progress"
  },
  "C2":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"OEM BDS initialization codes",
    "type":"Progress"
  },
  "C1":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"OEM BDS initialization codes",
    "type":"Progress"
  },
  "C0":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"OEM BDS initialization codes",
    "type":"Progress"
  },
  "C7":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"OEM BDS initialization codes",
    "type":"Progress"
  },
  "C6":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"OEM BDS initialization codes",
    "type":"Progress"
  },
  "C5":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"OEM BDS initialization codes",
    "type":"Progress"
  },
  "C4":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"OEM BDS initialization codes",
    "type":"Progress"
  },
  "CC":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"OEM BDS initialization codes",
    "type":"Progress"
  },
  "CB":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"OEM BDS initialization codes",
    "type":"Progress"
  },
  "CA":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"OEM BDS initialization codes",
    "type":"Progress"
  },
  "CF":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"OEM BDS initialization codes",
    "type":"Progress"
  },
  "CE":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"OEM BDS initialization codes",
    "type":"Progress"
  },
  "CD":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"OEM BDS initialization codes",
    "type":"Progress"
  },
  "99":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"Super IO Initialization",
    "type":"Progress"
  },
  "98":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"Console input devices connect",
    "type":"Progress"
  },
  "91":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"Driver connecting is started",
    "type":"Progress"
  },
  "90":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"Boot Device Selection (BDS) phase is started",
    "type":"Progress"
  },
  "93":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"PCI Bus Hot Plug Controller Initialization",
    "type":"Progress"
  },
  "92":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"PCI Bus initialization is started",
    "type":"Progress"
  },
  "95":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"PCI Bus Request Resources",
    "type":"Progress"
  },
  "94":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"PCI Bus Enumeration",
    "type":"Progress"
  },
  "97":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"Console Output devices connect",
    "type":"Progress"
  },
  "96":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"PCI Bus Assign Resources",
    "type":"Progress"
  },
  "F0":{
    "phase":"PEI Phase",
    "checkpoint":"Recovery (PEI)",
    "message":"Recovery condition triggered by firmware (Auto recovery)",
    "type":"Progress"
  },
  "F1":{
    "phase":"PEI Phase",
    "checkpoint":"Recovery (PEI)",
    "message":"Recovery condition triggered by user (Forced recovery)",
    "type":"Progress"
  },
  "F2":{
    "phase":"PEI Phase",
    "checkpoint":"Recovery (PEI)",
    "message":"Recovery process started",
    "type":"Progress"
  },
  "6C":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"North Bridge DXE initialization (North Bridge module specific)",
    "type":"Progress"
  },
  "6D":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"North Bridge DXE initialization (North Bridge module specific)",
    "type":"Progress"
  },
  "F5":{
    "phase":"PEI Phase",
    "checkpoint":"Recovery (PEI)",
    "message":"Reserved for future AMI progress codes",
    "type":"Progress"
  },
  "6F":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"North Bridge DXE initialization (North Bridge module specific)",
    "type":"Progress"
  },
  "F7":{
    "phase":"PEI Phase",
    "checkpoint":"Recovery (PEI)",
    "message":"Reserved for future AMI progress codes",
    "type":"Progress"
  },
  "F8":{
    "phase":"PEI Phase",
    "checkpoint":"Recovery Errors (PEI)",
    "message":"Recovery PPI is not availabled",
    "type":"Error"
  },
  "F9":{
    "phase":"PEI Phase",
    "checkpoint":"Recovery Errors (PEI)",
    "message":"Recovery capsule is not found",
    "type":"Error"
  },
  "7A":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"Reserved for future AMI DXE codes",
    "type":"Progress"
  },
  "BD":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"Reserved for future AMI codes",
    "type":"Progress"
  },
  "BE":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"Reserved for future AMI codes",
    "type":"Progress"
  },
  "BF":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"Reserved for future AMI codes",
    "type":"Progress"
  },
  "BA":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"Reserved for future AMI codes",
    "type":"Progress"
  },
  "BB":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"Reserved for future AMI codes",
    "type":"Progress"
  },
  "BC":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"Reserved for future AMI codes",
    "type":"Progress"
  },
  "5E":{
    "phase":"PEI Phase",
    "checkpoint":"PEI Errors",
    "message":"Reserved for future AMI error codes",
    "type":"Error"
  },
  "5D":{
    "phase":"PEI Phase",
    "checkpoint":"PEI Errors",
    "message":"Reserved for future AMI error codes",
    "type":"Error"
  },
  "5F":{
    "phase":"PEI Phase",
    "checkpoint":"PEI Errors",
    "message":"Reserved for future AMI error codes",
    "type":"Error"
  },
  "5A":{
    "phase":"PEI Phase",
    "checkpoint":"PEI Errors",
    "message":"Internal CPU error",
    "type":"Error"
  },
  "5C":{
    "phase":"PEI Phase",
    "checkpoint":"PEI Errors",
    "message":"PEI phase BMC self-test failure",
    "type":"Error"
  },
  "5B":{
    "phase":"PEI Phase",
    "checkpoint":"PEI Errors",
    "message":"reset PPI is not available",
    "type":"Error"
  },
  "24":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"OEM pre-memory initialization codes",
    "type":"Progress"
  },
  "25":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"OEM pre-memory initialization codes",
    "type":"Progress"
  },
  "26":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"OEM pre-memory initialization codes",
    "type":"Progress"
  },
  "27":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"OEM pre-memory initialization codes",
    "type":"Progress"
  },
  "20":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"OEM pre-memory initialization codes",
    "type":"Progress"
  },
  "21":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"OEM pre-memory initialization codes",
    "type":"Progress"
  },
  "22":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"OEM pre-memory initialization codes",
    "type":"Progress"
  },
  "23":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"OEM pre-memory initialization codes",
    "type":"Progress"
  },
  "28":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"OEM pre-memory initialization codes",
    "type":"Progress"
  },
  "29":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"OEM pre-memory initialization codes",
    "type":"Progress"
  },
  "2D":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"Memory initialization. Programming memory timing information",
    "type":"Progress"
  },
  "2E":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"Memory initialization. Configuring memory",
    "type":"Progress"
  },
  "2F":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"Memory initialization (other).",
    "type":"Progress"
  },
  "2A":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"OEM pre-memory initialization codes",
    "type":"Progress"
  },
  "2B":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"Memory initialization. Serial Presence Detect (SPD) data reading",
    "type":"Progress"
  },
  "2C":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"Memory initialization. Memory presence detection",
    "type":"Progress"
  },
  "59":{
    "phase":"PEI Phase",
    "checkpoint":"PEI Errors",
    "message":"CPU micro-code is not found or micro-code update is failed",
    "type":"Error"
  },
  "58":{
    "phase":"PEI Phase",
    "checkpoint":"PEI Errors",
    "message":"CPU self test failed or possible CPU cache error",
    "type":"Error"
  },
  "61":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"NVRAM initialization",
    "type":"Progress"
  },
  "55":{
    "phase":"PEI Phase",
    "checkpoint":"PEI Errors",
    "message":"Memory not installed",
    "type":"Error"
  },
  "54":{
    "phase":"PEI Phase",
    "checkpoint":"PEI Errors",
    "message":"Unspecified memory initialization error.",
    "type":"Error"
  },
  "57":{
    "phase":"PEI Phase",
    "checkpoint":"PEI Errors",
    "message":"CPU mismatch",
    "type":"Error"
  },
  "56":{
    "phase":"PEI Phase",
    "checkpoint":"PEI Errors",
    "message":"Invalid CPU type or Speed",
    "type":"Error"
  },
  "51":{
    "phase":"PEI Phase",
    "checkpoint":"PEI Errors",
    "message":"Memory initialization error. SPD reading has failed",
    "type":"Error"
  },
  "50":{
    "phase":"PEI Phase",
    "checkpoint":"PEI Errors",
    "message":"Memory initialization error. Invalid memory type or incompatible memory speed",
    "type":"Error"
  },
  "53":{
    "phase":"PEI Phase",
    "checkpoint":"PEI Errors",
    "message":"Memory initialization error. No usable memory detected",
    "type":"Error"
  },
  "52":{
    "phase":"PEI Phase",
    "checkpoint":"PEI Errors",
    "message":"Memory initialization error. Invalid memory size or memory modules do not match.",
    "type":"Error"
  },
  "B4":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"USB hot plug",
    "type":"Progress"
  },
  "B5":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"PCI bus hot plug",
    "type":"Progress"
  },
  "B6":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"Clean-up of NVRAM",
    "type":"Progress"
  },
  "63":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"CPU DXE initialization is started",
    "type":"Progress"
  },
  "B0":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"Runtime Set Virtual Address MAP Begin",
    "type":"Progress"
  },
  "B1":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"Runtime Set Virtual Address MAP End",
    "type":"Progress"
  },
  "B2":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"Legacy Option ROM Initialization",
    "type":"Progress"
  },
  "B3":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"System Reset",
    "type":"Progress"
  },
  "FD":{
    "phase":"PEI Phase",
    "checkpoint":"Recovery Errors (PEI)",
    "message":"Reserved for future AMI error codes",
    "type":"Error"
  },
  "B8":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"Reserved for future AMI codes",
    "type":"Progress"
  },
  "B9":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"Reserved for future AMI codes",
    "type":"Progress"
  },
  "65":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"CPU DXE initialization (CPU module specific)",
    "type":"Progress"
  },
  "66":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"CPU DXE initialization (CPU module specific)",
    "type":"Progress"
  },
  "88":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"OEM DXE initialization codes",
    "type":"Progress"
  },
  "89":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"OEM DXE initialization codes",
    "type":"Progress"
  },
  "82":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"OEM DXE initialization codes",
    "type":"Progress"
  },
  "83":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"OEM DXE initialization codes",
    "type":"Progress"
  },
  "80":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"OEM DXE initialization codes",
    "type":"Progress"
  },
  "81":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"OEM DXE initialization codes",
    "type":"Progress"
  },
  "86":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"OEM DXE initialization codes",
    "type":"Progress"
  },
  "87":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"OEM DXE initialization codes",
    "type":"Progress"
  },
  "84":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"OEM DXE initialization codes",
    "type":"Progress"
  },
  "85":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"OEM DXE initialization codes",
    "type":"Progress"
  },
  "B7":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"Configuration Reset (reset of NVRAM settings)",
    "type":"Progress"
  },
  "E9":{
    "phase":"PEI Phase",
    "checkpoint":"S3 Resume Errors (PEI)",
    "message":"S3 Resume Errors (PEI) PPI not Found",
    "type":"Error"
  },
  "E8":{
    "phase":"PEI Phase",
    "checkpoint":"S3 Resume Errors (PEI)",
    "message":"S3 Resume Errors (PEI) Failed",
    "type":"Error"
  },
  "E5":{
    "phase":"PEI Phase",
    "checkpoint":"S3 Resume (PEI)",
    "message":"Reserved for future AMI progress codes",
    "type":"Progress"
  },
  "E4":{
    "phase":"PEI Phase",
    "checkpoint":"S3 Resume (PEI)",
    "message":"Reserved for future AMI progress codes",
    "type":"Progress"
  },
  "E7":{
    "phase":"PEI Phase",
    "checkpoint":"S3 Resume (PEI)",
    "message":"Reserved for future AMI progress codes",
    "type":"Progress"
  },
  "E6":{
    "phase":"PEI Phase",
    "checkpoint":"S3 Resume (PEI)",
    "message":"Reserved for future AMI progress codes",
    "type":"Progress"
  },
  "E1":{
    "phase":"PEI Phase",
    "checkpoint":"S3 Resume (PEI)",
    "message":"S3 Boot Script execution",
    "type":"Progress"
  },
  "E0":{
    "phase":"PEI Phase",
    "checkpoint":"S3 Resume (PEI)",
    "message":"S3 Resume (PEI) is stared (S3 Resume (PEI) PPI is called by the DXE IPL)",
    "type":"Progress"
  },
  "E3":{
    "phase":"PEI Phase",
    "checkpoint":"S3 Resume (PEI)",
    "message":"OS S3 wake vector call",
    "type":"Progress"
  },
  "E2":{
    "phase":"PEI Phase",
    "checkpoint":"S3 Resume (PEI)",
    "message":"Video repost",
    "type":"Progress"
  },
  "EE":{
    "phase":"PEI Phase",
    "checkpoint":"S3 Resume Errors (PEI)",
    "message":"Reserved for future AMI error codes",
    "type":"Error"
  },
  "ED":{
    "phase":"PEI Phase",
    "checkpoint":"S3 Resume Errors (PEI)",
    "message":"Reserved for future AMI error codes",
    "type":"Error"
  },
  "EF":{
    "phase":"PEI Phase",
    "checkpoint":"S3 Resume Errors (PEI)",
    "message":"Reserved for future AMI error codes",
    "type":"Error"
  },
  "EA":{
    "phase":"PEI Phase",
    "checkpoint":"S3 Resume Errors (PEI)",
    "message":"S3 Resume Errors (PEI) Boot Script Error",
    "type":"Error"
  },
  "EC":{
    "phase":"PEI Phase",
    "checkpoint":"S3 Resume Errors (PEI)",
    "message":"Reserved for future AMI error codes",
    "type":"Error"
  },
  "EB":{
    "phase":"PEI Phase",
    "checkpoint":"S3 Resume Errors (PEI)",
    "message":"S3 OS Wake Error",
    "type":"Error"
  },
  "8B":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"OEM DXE initialization codes",
    "type":"Progress"
  },
  "8C":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"OEM DXE initialization codes",
    "type":"Progress"
  },
  "8A":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"OEM DXE initialization codes",
    "type":"Progress"
  },
  "8F":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"OEM DXE initialization codes",
    "type":"Progress"
  },
  "8D":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"OEM DXE initialization codes",
    "type":"Progress"
  },
  "8E":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"OEM DXE initialization codes",
    "type":"Progress"
  },
  "1A":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"Pre-memory South Bridge initialization (South Bridge module specific)",
    "type":"Progress"
  },
  "1C":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"Pre-memory South Bridge initialization (South Bridge module specific)",
    "type":"Progress"
  },
  "1B":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"Pre-memory South Bridge initialization (South Bridge module specific)",
    "type":"Progress"
  },
  "1E":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"OEM pre-memory initialization codes",
    "type":"Progress"
  },
  "1D":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"OEM pre-memory initialization codes",
    "type":"Progress"
  },
  "1F":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"OEM pre-memory initialization codes",
    "type":"Progress"
  },
  "4A":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"OEM post memory initialization codes",
    "type":"Progress"
  },
  "11":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"Pre-memory CPU initialization is started",
    "type":"Progress"
  },
  "10":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"PEI Core is started",
    "type":"Progress"
  },
  "13":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"Pre-memory CPU initialization (CPU module specific)",
    "type":"Progress"
  },
  "12":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"Pre-memory CPU initialization (CPU module specific)",
    "type":"Progress"
  },
  "15":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"Pre-memory North Bridge initialization is started",
    "type":"Progress"
  },
  "14":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"Pre-memory CPU initialization (CPU module specific)",
    "type":"Progress"
  },
  "17":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"Pre-Memory North Bridge initialization (North Bridge module specific)",
    "type":"Progress"
  },
  "16":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"Pre-Memory North Bridge initialization (North Bridge module specific)",
    "type":"Progress"
  },
  "19":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"Pre-memory South Bridge initialization is started",
    "type":"Progress"
  },
  "18":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution up to and including memory detection",
    "message":"Pre-Memory North Bridge initialization (North Bridge module specific)",
    "type":"Progress"
  },
  "62":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"Installation of the South Bridge Runtime Services",
    "type":"Progress"
  },
  "DB":{
    "phase":"DXE Phase",
    "checkpoint":"DXE errors",
    "message":"Flash update is failed",
    "type":"Error"
  },
  "DC":{
    "phase":"DXE Phase",
    "checkpoint":"DXE errors",
    "message":"Reset protocol is not available",
    "type":"Error"
  },
  "DA":{
    "phase":"DXE Phase",
    "checkpoint":"DXE errors",
    "message":"Boot Option is failed (StartImage returned error)",
    "type":"Error"
  },
  "7F":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"Reserved for future AMI DXE codes",
    "type":"Progress"
  },
  "7E":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"Reserved for future AMI DXE codes",
    "type":"Progress"
  },
  "7D":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"Reserved for future AMI DXE codes",
    "type":"Progress"
  },
  "7C":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"Reserved for future AMI DXE codes",
    "type":"Progress"
  },
  "7B":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"Reserved for future AMI DXE codes",
    "type":"Progress"
  },
  "48":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"OEM post memory initialization codes",
    "type":"Progress"
  },
  "49":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"OEM post memory initialization codes",
    "type":"Progress"
  },
  "46":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"OEM post memory initialization codes",
    "type":"Progress"
  },
  "47":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"OEM post memory initialization codes",
    "type":"Progress"
  },
  "44":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"OEM post memory initialization codes",
    "type":"Progress"
  },
  "45":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"OEM post memory initialization codes",
    "type":"Progress"
  },
  "42":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"OEM post memory initialization codes",
    "type":"Progress"
  },
  "43":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"OEM post memory initialization codes",
    "type":"Progress"
  },
  "40":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"OEM post memory initialization codes",
    "type":"Progress"
  },
  "41":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"OEM post memory initialization codes",
    "type":"Progress"
  },
  "A1":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"IDE Reset",
    "type":"Progress"
  },
  "A0":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"IDE initialization is started",
    "type":"Progress"
  },
  "A3":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"IDE Enable",
    "type":"Progress"
  },
  "A2":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"IDE Detect",
    "type":"Progress"
  },
  "A5":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"SCSI Reset",
    "type":"Progress"
  },
  "A4":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"SCSI initialization is started",
    "type":"Progress"
  },
  "A7":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"SCSI Enable",
    "type":"Progress"
  },
  "A6":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"SCSI Detect",
    "type":"Progress"
  },
  "A9":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"Start of Setup",
    "type":"Progress"
  },
  "A8":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"Setup Verifying Password",
    "type":"Progress"
  },
  "AA":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"Reserved for ASL",
    "type":"Progress"
  },
  "AC":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"Reserved for ASL",
    "type":"Progress"
  },
  "AB":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"Setup Input Wait",
    "type":"Progress"
  },
  "AE":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"Legacy Boot event",
    "type":"Progress"
  },
  "AD":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"Ready To Boot event",
    "type":"Progress"
  },
  "AF":{
    "phase":"DXE Phase",
    "checkpoint":"BDS execution",
    "message":"Exit Boot Services event",
    "type":"Progress"
  },
  "77":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"South Bridge DXE Initialization (South Bridge module specific)",
    "type":"Progress"
  },
  "76":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"South Bridge DXE Initialization (South Bridge module specific)",
    "type":"Progress"
  },
  "75":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"South Bridge DXE Initialization (South Bridge module specific)",
    "type":"Progress"
  },
  "74":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"South Bridge DXE Initialization (South Bridge module specific)",
    "type":"Progress"
  },
  "73":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"South Bridge DXE Initialization (South Bridge module specific)",
    "type":"Progress"
  },
  "72":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"South Bridge devices initialization",
    "type":"Progress"
  },
  "71":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"South Bridge DXE SMM initialization is started",
    "type":"Progress"
  },
  "70":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"South Bridge DXE initialization is started",
    "type":"Progress"
  },
  "4F":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"DXE IPL is started",
    "type":"Progress"
  },
  "4D":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"OEM post memory initialization codes",
    "type":"Progress"
  },
  "4E":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"OEM post memory initialization codes",
    "type":"Progress"
  },
  "4B":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"OEM post memory initialization codes",
    "type":"Progress"
  },
  "4C":{
    "phase":"PEI Phase",
    "checkpoint":"PEI execution after memory detection",
    "message":"OEM post memory initialization codes",
    "type":"Progress"
  },
  "79":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"CSM initialization",
    "type":"Progress"
  },
  "78":{
    "phase":"DXE Phase",
    "checkpoint":"DXE execution up to BDS",
    "message":"ACPI module initialization",
    "type":"Progress"
  },
  "D8":{
    "phase":"DXE Phase",
    "checkpoint":"DXE errors",
    "message":"Invalid password",
    "type":"Error"
  },
  "D9":{
    "phase":"DXE Phase",
    "checkpoint":"DXE errors",
    "message":"Error loading Boot Option (LoadImage returned error)",
    "type":"Error"
  },
  "D6":{
    "phase":"DXE Phase",
    "checkpoint":"DXE errors",
    "message":"No Console Output Devices are found",
    "type":"Error"
  },
  "D7":{
    "phase":"DXE Phase",
    "checkpoint":"DXE errors",
    "message":"No Console Input Devices are found",
    "type":"Error"
  },
  "D4":{
    "phase":"DXE Phase",
    "checkpoint":"DXE errors",
    "message":"PCI resource allocation error. Out of Resources",
    "type":"Error"
  },
  "D5":{
    "phase":"DXE Phase",
    "checkpoint":"DXE errors",
    "message":"No Space for Legacy Option ROM",
    "type":"Error"
  },
  "D2":{
    "phase":"DXE Phase",
    "checkpoint":"DXE errors",
    "message":"South Bridge initialization error",
    "type":"Error"
  },
  "D3":{
    "phase":"DXE Phase",
    "checkpoint":"DXE errors",
    "message":"Some of the Architectural Protocols are not available",
    "type":"Error"
  },
  "D0":{
    "phase":"DXE Phase",
    "checkpoint":"DXE errors",
    "message":"CPU initialization error",
    "type":"Error"
  },
  "D1":{
    "phase":"DXE Phase",
    "checkpoint":"DXE errors",
    "message":"North Bridge initialization error",
    "type":"Error"
  }
}'''
jsonToPython = json.loads(jsonData)

try:
  print(jsonToPython[sys.argv[1].upper()]['message'])
  print(jsonToPython[sys.argv[1].upper()]['phase'])
  print(jsonToPython[sys.argv[1].upper()]['checkpoint'])
  print(jsonToPython[sys.argv[1].upper()]['type'])
except:
  pass
