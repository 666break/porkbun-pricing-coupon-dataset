# Porkbun pricing and coupon-code test data

Dated, source-attributed datasets on Porkbun domain prices and coupon-code behaviour. Every figure was read from a live Porkbun page or a live checkout cart on the stated date. Nothing here is estimated.

Transcribed from the dated tables at [couponbun.com](https://couponbun.com/) and [couponbun.com/porkbun-first-year-vs-renewal-price](https://couponbun.com/porkbun-first-year-vs-renewal-price).

## Files

| File | What it contains | Read date |
| --- | --- | --- |
| `porkbun-tld-prices-2026-11-22.csv` | First-year, regular and renewal price fields for six TLDs, from each TLD's own page on porkbun.com | 2026-11-22 |
| `porkbun-coupon-code-tests-2026-11-21.md` | 24 coupon codes submitted one at a time to the live checkout code box, cart total before and after each | 2026-11-21 |
| `gap_report.py` | Standard-library CLI that reads the CSV and prints rows sorted by first-year-to-renewal gap | - |

## Where the numbers came from

- `porkbun-tld-prices-2026-11-22.csv`: the `Registration, first year`, `Registration, regular price` and `Renewal` fields printed on `porkbun.com/tld/<tld>`. Each field was captured in two separate sessions on 2026-11-22 and every TLD matched across both reads. The `.com` page prints a single `Registration` field of $11.81 and a `Renewal` of $11.81, with no first-year/regular split; that row is marked in the `note` column.
- `porkbun-coupon-code-tests-2026-11-21.md`: each of 24 codes was submitted once to the live `#cartCouponCode` box at `porkbun.com/checkout/cart` on 2026-11-21, against a fresh one-year registration of `couponhunt8842xyz.org`. The cart was reset before every code. A cart total of $6.98 (`data-row-price-increment` 698) means the code worked; $7.98 (798) means it did nothing.

## Derived columns

The CSV carries two calculated columns, both computed from the two official fields on the same row:

- `two_year_total_usd = first_year_usd + renewal_usd`
- `gap_usd = renewal_usd - first_year_usd`

Example, `.org`: $7.98 + $11.84 = $19.82; $11.84 - $7.98 = $3.86. The two inputs are the `Registration, first year` and `Renewal` fields on `porkbun.com/tld/org`, read 2026-11-22.

## Running the tool

```sh
python3 gap_report.py
```

No third-party packages. Pass `--csv PATH` to read a different copy of the data.

## Caveat

Prices and coupon eligibility can change at any time. These are the values on the dates above; re-read the live fields before relying on them.
