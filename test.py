import openff.toolkit

popc = openff.toolkit.Molecule.from_smiles(
    r"CCCCCCCCCCCCCCCC(=O)OC[C@H](COP(=O)([O-])OCC[N+](C)(C)C)OC(=O)CCCCCCC/C=C\CCCCCCCC",
    allow_undefined_stereo=True,
)
popc.generate_conformers()

openmm_system = openff.toolkit.ForceField("openff-2.3.0.offxml").create_openmm_system(
    popc.to_topology()
)

print(f"Made OpenMM system with {len(openmm_system.getForces())} forces "
      f"and {openmm_system.getNumParticles()} particles")