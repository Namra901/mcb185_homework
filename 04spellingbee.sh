gzip -cd "/Users/namrazahoor/Desktop/MCB185/data/dictionary.gz" | \
grep 'r' | \
grep -v '[^orzincar]' | \
grep -E '^.{4,}$' | \
grep -i '^[orzincar]*r[orzincar]*$'
