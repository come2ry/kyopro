/**
 * @brief Succinct Indexable Dictionary(完備辞書)
 */

void print() {
  cout << endl;
}

template <class Head, class... Tail>
void print(Head&& head, Tail&&... tail) {
  cout << head;
  if (sizeof...(tail) != 0) cout << ", ";
  print(forward<Tail>(tail)...);
}

template <class T>
void print(vector<T> &vec) {
  cout << "[";
  for (auto& a : vec) {
    cout << a;
    if (&a != &vec.back()) cout << ", ";
  }
  cout << "]" << endl;
}

template <class T>
void print(vector<vector<T>> &df) {
  for (auto& vec : df) {
    print(vec);
  }
}

struct SuccinctIndexableDictionary {
  size_t length;
  size_t blocks;
  vector< unsigned > bit, sum;

  SuccinctIndexableDictionary() = default;

  SuccinctIndexableDictionary(size_t length) : length(length), blocks((length + 31) >> 5) {
    bit.assign(blocks, 0U);
    sum.assign(blocks, 0U);
    std::cout << "length: " << length << ", blocks: " << blocks << std::endl;
    std::cout << "bit: ";
    print(bit);
    std::cout << "sum: ";
    print(sum);
  }

  void set(int k) {
    bit[k >> 5] |= 1U << (k & 31);
    std::cout << "k, " << k << ", bit: ";
    print(bit);
  }

  void build() {
    sum[0] = 0U;
    for(int i = 1; i < blocks; i++) {
      sum[i] = sum[i - 1] + __builtin_popcount(bit[i - 1]);
    }
  }

  bool operator[](int k) {
    return (bool((bit[k >> 5] >> (k & 31)) & 1));
  }

  int rank(int k) {
    std::cout << "k: " << k << std::endl;
    std::cout << "k >> 5: " << (k >> 5) << std::endl;
    std::cout << "sum[k >> 5]: " << sum[k >> 5] << std::endl;
    std::cout << "bit: ";
    print(bit);
    std::cout << "bit[k >> 5]: " << bit[k >> 5] << std::endl;
    auto t = ((1U << (k & 31)) - 1);
    std::cout << "((1U << (k & 31)) - 1): " << t << std::endl;
    std::cout << "__builtin_popcount: " << __builtin_popcount(bit[k >> 5] & t) << std::endl;
    return (sum[k >> 5] + __builtin_popcount(bit[k >> 5] & ((1U << (k & 31)) - 1)));
  }

  int rank(bool val, int k) {
    std::cout << "val: " << val << ", k: " << k << std::endl;
    auto t = rank(k);
    std::cout << "rank(k): " << t << std::endl;
    return (val ? t : k - t);
  }
};