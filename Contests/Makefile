#!/bin/bash

CONTEST=abc229
GEN_DIR=/Users/tkrk/Document_local/Documents/kyopro/Contests
TEMPLATE=${GEN_DIR}/template/my_template.j2
ATT=atcoder-tools
PROBLEM=A
ACTION=submit
OPT=

gen:
	echo "${TEMPLATE}"
	${ATT} gen ${CONTEST} --lang python --template ${TEMPLATE} --workspace ${GEN_DIR} --skip-existing-problems --parallel
	echo "A/\nB/\nC/\nD/\nE/\nF/\nG/\nH/\nI/\nJ/\nEx/\ntest/" > ${GEN_DIR}/${CONTEST}/.gitignore
	find ./${CONTEST} -name "main.py" | sed 's/\// /g' | awk '{print "sed -i \"\" -e \"s/\\[contest_id\\]/${CONTEST}/g\" -e \"s/\\[problem\\]/"$$3"/g\" ${CONTEST}/"$$3"/main.py"}' | sh

X:
	cd ${CONTEST}/${PROBLEM}; \
	${ATT} ${ACTION} ${OPT}; \
	if [ "$$?" = "0" ]; then \
		sed -i '' -e "/${PROBLEM}\//d" ../.gitignore; \
	fi;

A:
	$(MAKE) X PROBLEM=A ACTION=${ACTION}
B:
	$(MAKE) X PROBLEM=B ACTION=${ACTION}
C:
	$(MAKE) X PROBLEM=C ACTION=${ACTION}
D:
	$(MAKE) X PROBLEM=D ACTION=${ACTION}
E:
	$(MAKE) X PROBLEM=E ACTION=${ACTION}
F:
	$(MAKE) X PROBLEM=F ACTION=${ACTION}
G:
	$(MAKE) X PROBLEM=G ACTION=${ACTION}
H:
	$(MAKE) X PROBLEM=H ACTION=${ACTION}
I:
	$(MAKE) X PROBLEM=I ACTION=${ACTION}
J:
	$(MAKE) X PROBLEM=J ACTION=${ACTION}
Ex:
	$(MAKE) X PROBLEM=Ex ACTION=${ACTION}

A-u:
	$(MAKE) X PROBLEM=A ACTION=${ACTION} OPT=-u
B-u:
	$(MAKE) X PROBLEM=B ACTION=${ACTION} OPT=-u
C-u:
	$(MAKE) X PROBLEM=C ACTION=${ACTION} OPT=-u
D-u:
	$(MAKE) X PROBLEM=D ACTION=${ACTION} OPT=-u
E-u:
	$(MAKE) X PROBLEM=E ACTION=${ACTION} OPT=-u
F-u:
	$(MAKE) X PROBLEM=F ACTION=${ACTION} OPT=-u
G-u:
	$(MAKE) X PROBLEM=G ACTION=${ACTION} OPT=-u
H-u:
	$(MAKE) X PROBLEM=H ACTION=${ACTION} OPT=-u
I-u:
	$(MAKE) X PROBLEM=I ACTION=${ACTION} OPT=-u
J-u:
	$(MAKE) X PROBLEM=J ACTION=${ACTION} OPT=-u
Ex-u:
	$(MAKE) X PROBLEM=Ex ACTION=${ACTION} OPT=-u

A-test:
	$(MAKE) X PROBLEM=A ACTION=test
B-test:
	$(MAKE) X PROBLEM=B ACTION=test
C-test:
	$(MAKE) X PROBLEM=C ACTION=test
D-test:
	$(MAKE) X PROBLEM=D ACTION=test
E-test:
	$(MAKE) X PROBLEM=E ACTION=test
F-test:
	$(MAKE) X PROBLEM=F ACTION=test
G-test:
	$(MAKE) X PROBLEM=G ACTION=test
H-test:
	$(MAKE) X PROBLEM=H ACTION=test
I-test:
	$(MAKE) X PROBLEM=I ACTION=test
J-test:
	$(MAKE) X PROBLEM=J ACTION=test
Ex-test:
	$(MAKE) X PROBLEM=Ex ACTION=test

COMMIT:
	dir_path="${GEN_DIR}/${CONTEST}"; \
	cd $${dir_path}; \
	dirs=$$(ls ./ | sort); \
	for dir in $$dirs; do \
		cd ${GEN_DIR}; \
		$(MAKE) $${dir}-test; \
		if [ "$$?" = "0" ]; then \
			git add ${GEN_DIR}/${CONTEST}/.gitignore; \
			git add ${GEN_DIR}/${CONTEST}/$${dir}; \
			git commit -m "AC: ${CONTEST}_$${dir}"; \
		else \
			echo [SKIP] $${dir}; \
		fi; \
	done