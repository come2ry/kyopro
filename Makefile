CONTEST=abc228
GEN_DIR=/Users/tkrk/Document_local/Documents/kyopuro/Contests
ATT=atcoder-tools

gen:
	${ATT} gen ${CONTEST} --workspace ${GEN_DIR}
	echo "cd ${GEN_DIR}" | pbcopy
