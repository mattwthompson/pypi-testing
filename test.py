import time
from functools import wraps
import openff.toolkit


def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Function '{func.__name__}' took {end - start:.6f} seconds.")
        return result

    return wrapper


@time_it
def load_sage():
    openff.toolkit.ForceField("openff-2.3.0.offxml")


@time_it
def build_single_popc():
    popc_molecule = openff.toolkit.Molecule.from_smiles(
        r"CCCCCCCCCCCCCCCC(=O)OC[C@H](COP(=O)([O-])OCC[N+](C)(C)C)OC(=O)CCCCCCC/C=C\CCCCCCCC",
        allow_undefined_stereo=True,
    )
    popc_molecule.generate_conformers()

    openmm_system = openff.toolkit.ForceField(
        "openff-2.3.0.offxml"
    ).create_openmm_system(popc_molecule.to_topology())


@time_it
def build_gb3():
    openff.toolkit.ForceField("openff-2.3.0.offxml").create_openmm_system(
        openff.toolkit.Topology.from_pdb("gb3-1P7E.pdb")
    )


load_sage()
build_single_popc()
build_gb3()
