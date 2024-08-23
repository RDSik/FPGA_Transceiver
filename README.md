![My Image](pic/transeiver.drawio.png)

# Usage

## Dependencies 

`hdlmake`, `make`, `cocotb`, `vivado`, `modelsim`, `python`

## Installation

### Clone repository:
```bash
git clone --recurse-submodules https://github.com/RDSik/FPGA_transceiver.git
```

### Download pip:
```bash
https://pip.pypa.io/en/latest/installation/
```

### Download packages:
```bash
pip install six
pip install hdlmake
pip install cocotb
pip install pytest
```

### Download make (add to PATH system variable the Make bin folder: C:\Program Files (x86)\GnuWin32\bin):
```bash
winget install GnuWin32.make
```

## Build project

### Build trasceiver:
```bash
cd syn
hdlmake
make
```

### Build only vivado project:
```bash
cd syn
hdlmake
make project
```

## Simulation

### Vivado simulation using hdlmake:
```bash
cd top/sim/vivado
hdlmake
make
```

### Modelsim simulation using cocotb:
```bash
py -m venv myenv
.\myenv\Scripts\activate.ps1
cd sim\cocotb
py -m pytest test.py
deactivate
```
