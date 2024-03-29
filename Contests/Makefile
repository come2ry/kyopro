#!/bin/bash

CONTEST=abc324
GEN_DIR=/Users/tkrk/Document_local/Documents/kyopro/Contests
TEMPLATE=/Users/tkrk/Document_local/Documents/kyopro/template/my_template.j2
CMD=atcoder-tools
PROBLEM=A
ACTION=submit
OPT=
PARALLEL_NUM=8
CHROME_PATH=/Applications/Google Chrome.app


gen:
	echo "${TEMPLATE}"
	${CMD} gen ${CONTEST} --lang python --template ${TEMPLATE} --workspace ${GEN_DIR} --parallel
	echo "A/\nB/\nC/\nD/\nE/\nF/\nG/\nH/\nI/\nJ/\nEx/" > ${GEN_DIR}/${CONTEST}/.gitignore
	find ./${CONTEST} -name "main.py" | sed 's/\// /g' | awk '{print "sed -i \"\" -e \"s/\\[contest_id\\]/${CONTEST}/g\" -e \"s/\\[problem\\]/"$$3"/g\" ${CONTEST}/"$$3"/main.py"}' | sh

	dir_path="${GEN_DIR}/${CONTEST}"; \
	cd $${dir_path}; \
	dirs=$$(ls ./ | sort); \
	for dir in $$dirs; do \
		pushd $${dir}; \
		oj-template -t generate.py "https://atcoder.jp/contests/${CONTEST}/tasks/${CONTEST}_$${dir}" > ./generate.py; \
		chmod 0744 ./generate.py; \
		popd; \
	done

open:
	open -a '${CHROME_PATH}' https://atcoder.jp/contests/${CONTEST}
	open -a '${CHROME_PATH}' https://atcoder.jp/contests/${CONTEST}/tasks
	open -a '${CHROME_PATH}' https://atcoder.jp/contests/${CONTEST}/tasks/${CONTEST}_a
	open -a '${CHROME_PATH}' https://atcoder.jp/contests/${CONTEST}/tasks/${CONTEST}_b
	open -a '${CHROME_PATH}' https://atcoder.jp/contests/${CONTEST}/tasks/${CONTEST}_c
	open -a '${CHROME_PATH}' https://atcoder.jp/contests/${CONTEST}/tasks/${CONTEST}_d
	open -a '${CHROME_PATH}' https://atcoder.jp/contests/${CONTEST}/tasks/${CONTEST}_e
	open -a '${CHROME_PATH}' https://atcoder.jp/contests/${CONTEST}/tasks/${CONTEST}_f
	open -a '${CHROME_PATH}' https://atcoder.jp/contests/${CONTEST}/submissions/me
	open -a '${CHROME_PATH}' https://atcoder.jp/contests/${CONTEST}/standings


X:
	cd ${CONTEST}/${PROBLEM}; \
	${CMD} ${ACTION} ${OPT}; \
	result=$$?; \
	if [ "${CMD}" == "atcoder-tools" ]; then \
		if [ "$$result" = "0" ]; then \
			sed -i '' -e "/${PROBLEM}\//d" ../.gitignore; \
		fi; \
		exit $$result; \
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

A-gi:
	$(MAKE) X PROBLEM=A CMD=oj ACTION=g/i OPT='./generate.py --hack "python3 main.py" -j ${PARALLEL_NUM}'
B-gi:
	$(MAKE) X PROBLEM=B CMD=oj ACTION=g/i OPT='./generate.py --hack "python3 main.py" -j ${PARALLEL_NUM}'
C-gi:
	$(MAKE) X PROBLEM=C CMD=oj ACTION=g/i OPT='./generate.py --hack "python3 main.py" -j ${PARALLEL_NUM}'
D-gi:
	$(MAKE) X PROBLEM=D CMD=oj ACTION=g/i OPT='./generate.py --hack "python3 main.py" -j ${PARALLEL_NUM}'
E-gi:
	$(MAKE) X PROBLEM=E CMD=oj ACTION=g/i OPT='./generate.py --hack "python3 main.py" -j ${PARALLEL_NUM}'
F-gi:
	$(MAKE) X PROBLEM=F CMD=oj ACTION=g/i OPT='./generate.py --hack "python3 main.py" -j ${PARALLEL_NUM}'
G-gi:
	$(MAKE) X PROBLEM=G CMD=oj ACTION=g/i OPT='./generate.py --hack "python3 main.py" -j ${PARALLEL_NUM}'
H-gi:
	$(MAKE) X PROBLEM=H CMD=oj ACTION=g/i OPT='./generate.py --hack "python3 main.py" -j ${PARALLEL_NUM}'
I-gi:
	$(MAKE) X PROBLEM=I CMD=oj ACTION=g/i OPT='./generate.py --hack "python3 main.py" -j ${PARALLEL_NUM}'
J-gi:
	$(MAKE) X PROBLEM=J CMD=oj ACTION=g/i OPT='./generate.py --hack "python3 main.py" -j ${PARALLEL_NUM}'
Ex-gi:
	$(MAKE) X PROBLEM=Ex CMD=oj ACTION=g/i OPT='./generate.py --hack "python3 main.py" -j ${PARALLEL_NUM}'

COMMIT:
	git add ${GEN_DIR}/${CONTEST}/.gitignore; \
	git commit -m "UPDATE: ${CONTEST} .gitignore"; \
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

setup:
	pip3 install git+https://github.com/come2ry/atcoder-tools@stable
