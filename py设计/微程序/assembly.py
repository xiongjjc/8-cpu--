import pin

FETCH = [
    pin.PCOUT | pin.MARIN,
    pin.RAMOUT | pin.IRIN | pin.PCINC,
    pin.PCOUT | pin.MARIN,
    pin.RAMOUT | pin.DSTIN | pin.PCINC,
    pin.PCOUT | pin.MARIN,
    pin.RAMOUT | pin.SRCIN | pin.PCINC,
]
