import dropbox
import os
import errno
import wget

CONTEST_NAME = "abc231"
PROBLEM_NAME = "f"
OUT_PATH = "/Users/tkrk/Document_local/Documents/kyopro/Contests/testcase"
# AtCoder の Dropbox のリンク
SHARED_URL = "https://www.dropbox.com/sh/arnpe0ef5wds8cv/AAAk_SECQ2Nc6SVGii3rHX6Fa?dl=0"
DOWNLOAD_URL = "https://www.dropbox.com/sh/arnpe0ef5wds8cv/AAAk_SECQ2Nc6SVGii3rHX6Fa"


def ensure_dir(dirname):
    """
    Ensure that a named directory exists; if it does not, attempt to create it.
    """
    try:
        os.makedirs(dirname)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise e


def main(dbx):
    # 各コンテストの情報が格納された配列
    contests = dbx.files_list_folder(
        path="",
        shared_link=dropbox.files.SharedLink(url=SHARED_URL, password=None)
    ).entries

    contests_name_dict = dict([(c.name.lower(), c) for c in contests])
    contest = contests_name_dict.get(CONTEST_NAME, None)
    assert (contest is not None), f"ERROR: CONTEST_NAME({CONTEST_NAME})は存在しません"

    # あるコンテスト内の各問題の情報が格納された配列
    problems = dbx.files_list_folder(
        path=f"/{contest.name}",
        shared_link=dropbox.files.SharedLink(url=SHARED_URL, password=None)
    ).entries

    problems_name_dict = dict([(p.name.lower(), p) for p in problems])
    problem = problems_name_dict.get(PROBLEM_NAME, None)
    assert (problem is not None), f"ERROR: PROBLEM__NAME({PROBLEM_NAME})は存在しません"

    OUT_DIR_PATH = f"{OUT_PATH}/{contest.name}_{problem.name}"
    ensure_dir(OUT_DIR_PATH)

    # 各テストケースの標準入力側が格納された配列
    in_testcases = dbx.files_list_folder(
        path=f"/{contest.name}/{problem.name}/in",
        shared_link=dropbox.files.SharedLink(url=SHARED_URL, password=None)
    )

    # # 各テストケースの標準入力側をダウンロードする
    # for i, testcase in enumerate(in_testcases.entries):
    #     file_path = f"{OUT_PATH}/{contest.name}_{problem.name}/" + '.'.join(testcase.name.split('.')[:-1]) + '.in'
    #     download_url = f"{DOWNLOAD_URL}/{contest.name}/{problem.name}/in/{testcase.name}?dl=0"

    #     data = dbx.sharing_get_shared_link_file(
    #         url=SHARED_URL,
    #         path=f"/{contest.name}/{problem.name}/in/{testcase.name}"
    #     )
    #     print(data)
    #     # print(f"out/{testcase.name} -> ...", end="")

    #     # try:
    #     #     _ = wget.download(download_url, file_path)
    #     # except Exception as e:
    #     #     raise e
    #     # print("DONE")

    # # # 各テストケースの標準出力側が格納された配列
    # # out_testcases = dbx.files_list_folder(
    # #     path=f"/{contest.name}/{problem.name}/out",
    # #     shared_link=dropbox.files.SharedLink(url=SHARED_URL, password=None)
    # # )
    # # # 各テストケースの標準出力側をダウンロードする
    # # for _, testcase in enumerate(out_testcases.entries):
    # #     file_path = f"{OUT_PATH}/{contest.name}_{problem.name}/" + '.'.join(testcase.name.split('.')[:-1]) + '.out'
    # #     download_url = f"{DOWNLOAD_URL}/{contest.name}/{problem.name}/in/{testcase.name}?dl=0"
    # #     print(f"in/{testcase.name} -> ...", end="")

    # #     try:
    # #         _ = wget.download(download_url, file_path)
    # #     except Exception as e:
    # #         raise e
    # #     print("DONE")


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dropbox-token', dest='dbt', type=str, required=True)
    args = parser.parse_args()
    print(args.dbt)

    dbx = dropbox.Dropbox(args.dbt, scope=["sharing.read", "files.metadata.read"])
    main(dbx)
