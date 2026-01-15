import pin

FETCH = [
    pin.PCOUT | pin.MARIN,
    pin.RAMOUT | pin.IRIN | pin.PCINC,
    pin.PCOUT | pin.MARIN,
    pin.RAMOUT | pin.DSTIN | pin.PCINC,
    pin.PCOUT | pin.MARIN,
    pin.RAMOUT | pin.SRCIN | pin.PCINC,
]

MOV = 0 | pin.ADDR2
ADD = (1 << pin.ADDR2SHIFT) | pin.ADDR2

NOP = 0
HLT = 0x3f

INSTRUCTIONS = {
    2: {
        MOV: {
            (pin.AMREG, pin.AMINS): [
                pin.DSTW | pin.SRCOUT,
            ]
        }
    },
    1: {},
    0: {
        NOP: [
            pin.CYC,
        ],
        HLT: [
            pin.HLT,
        ]
    }
}