#!/bin/bash
### A hacky way to copy env.yml to the remote server
sed ':a;N;$!ba;s/\n/\\n/g' env.yml > tmp.yml
env=`cat tmp.yml`
pattern="%setup\\necho \"${env}\" > env.yml"

sed "4s/$/$pattern/" videogeneration.def > tmp.def

module load singularity
singularity build --remote videogeneration.sif tmp.def
rm tmp.yml tmp.def

