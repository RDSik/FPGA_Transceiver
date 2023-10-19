# Usage

## Dependencies 

`hdlmake`, `make`, `vivado`, `modelsim`, `python`

## Installation

Installation from git:

    git clone https://github.com/RDSik/FPGA_transceiver.git

Installation pip:

  https://pip.pypa.io/en/latest/installation/

Installation six:

    pip install six
    
Installation hdlmake:

    pip install hdlmake

Installation make (add to PATH system variable the Make bin folder: C:\Program Files (x86)\GnuWin32\bin):

    winget install GnuWin32.make

## Build trasceiver:
```bash
cd syn
hdlmake
make # make project create only Vivado project
```

## Build only vivado project:
```bash
cd syn
hdlmake
make project
```

## Trasceiver test
```bash
cd top/sim
hdlmake
make
vsim work.transceiver_tb
```
