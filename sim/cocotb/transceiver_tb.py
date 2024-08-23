import cocotb
import random
from cocotb.clock import Clock
from cocotb.triggers import Timer, RisingEdge, FallingEdge, ClockCycles
from cocotb.utils import get_sim_time

@cocotb.test()
async def test_transceiver(dut):

    clk_per  = 2
    sim_time = 25000
    
    cocotb.start_soon(Clock(dut.clk, clk_per, units = 'sec').start())

    # Reset
    async def reset(cycles):
        await FallingEdge(dut.clk)
        dut.arstn.value = 0
        await ClockCycles(dut.clk, cycles)
        dut.arstn.value = 1

    # Input data generation
    async def data_gen(time):
        dut.en.value = 1
        for i in range(time):
            dut.data.value = random.randint(0, 1)
            print(f"uart_rx_out={dut.uart_rx_out}, encoder_out={dut.encoder_out}, decoder_out={dut.decoder_out}, demodulator_out={dut.demodulator_out}, active={dut.active}, data_valid={dut.data_valid}, done={dut.done}")
            await Timer(clk_per/2, units="sec")
        dut.en.value = 0
        print(f'Generation ended at {get_sim_time('sec')} sec.')

    #------------------Order of test execution -------------------
    dut.en.value = 0
    await reset(1)
    await RisingEdge(dut.clk)
    await data_gen(sim_time)
