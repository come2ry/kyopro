#define PROBLEM "http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1549"

#include "../../template/template.cpp"

#include "../../structure/wavelet/wavelet-matrix.cpp"

int main() {
  int n;
  cin >> n;

  const int OFS = 1e6;
  vector< int > as(n);
  for(int i = 0; i < n; i++) cin >> as[i], as[i] += OFS;
  CompressedWaveletMatrix< int, 17 > wm(as);

  int q;
  cin >> q;
  for(int i = 0; i < q; i++) {
    std::cout << "i: " << i << std::endl;
    int l, r, d;
    cin >> l >> r >> d;
    r++;
    d += OFS;
    int ans = OFS * 2;
    std::cout << "wm.rank(d, l): " << wm.rank(d, l) <<std::endl;
    std::cout << "wm.rank(d, r): " << wm.rank(d, r) <<std::endl;
    if(wm.rank(d, l) < wm.rank(d, r)) {
      ans = 0;
    } else {
      int succ = wm.next_value(l, r, d);
      std::cout << "succ: " << succ <<std::endl;
      if(~succ) chmin(ans, abs(succ - d));
      std::cout << "ans: " << ans <<std::endl;
      int pred = wm.prev_value(l, r, d);
      std::cout << "pred: " << pred <<std::endl;
      if(~pred) chmin(ans, abs(pred - d));
      std::cout << "ans: " << ans <<std::endl;
    }
    cout << ans << "\n";
  }
}