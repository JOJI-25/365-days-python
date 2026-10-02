import pandas as pd

data = {
    "order_id": range(801, 813),
    "customer_segment": [
        "New", "Regular", "Premium", "New",
        "Regular", "Premium", "New", "Regular",
        "Premium", "Regular", "New", "Premium"
    ],
    "items": [5, 12, 18, 4, 10, 21, 7, 15, 19, 9, 6, 24],
    "basket_value": [
        620, 1450, 2800, 510, 1320, 3150,
        780, 1750, 2950, 1100, 690, 3400
    ],
    "delivery_fee": [
        60, 40, 20, 70, 35, 15,
        55, 30, 15, 40, 65, 10
    ],
    "discount": [
        0, 100, 250, 0, 80, 300,
        50, 120, 200, 50, 0, 350
    ]
}

df = pd.DataFrame(data)

# Create a net_value column representing basket_value - discount + delivery_fee, and calculate the overall average net order value.

df['net_value'] = df['basket_value'] - df['discount'] + df['delivery_fee']
avg_net_value = df['net_value'].mean()
print(f"Overall average net order value: ₹{avg_net_value:.2f}")
print(df[['order_id', 'basket_value', 'discount', 'delivery_fee', 'net_value']])

# Compare the three customer segments using average basket value, average discount, average delivery fee, and average number of items.

customer_segments = df.groupby("customer_segment").agg(
    average_basket_value = ('basket_value', 'mean'),
    average_discount = ('discount', 'mean'),
    average_delivery_fee = ('delivery_fee', 'mean'),
    average_items = ('items', 'mean')
)

print("\n--- Comparison of Customer Segments ---")
print(customer_segments)

# Calculate the discount percentage relative to basket value for every order and identify the order receiving the largest relative discount.

df['discount_pct'] = (df['discount'] / df['basket_value']) * 100
max_discount_order = df.loc[df['discount_pct'].idxmax()]

print("--- 3. Discount Percentages & Max Discount Order ---")
print(df[['order_id', 'customer_segment', 'basket_value', 'discount', 'discount_pct']])
print(
    f"\nOrder receiving the largest relative discount: Order"
    f" {int(max_discount_order['order_id'])} "
    f"({max_discount_order['customer_segment']}) with"
    f" {max_discount_order['discount_pct']:.2f}% discount\n"
)

# Create a segment-level summary containing total revenue, total discounts, and average net order value, then determine which segment contributes the most total net value.

segment_summary = df.groupby('customer_segment').agg(
    total_basket_value=('basket_value', 'sum'),
    total_discounts=('discount', 'sum'),
    avg_net_value=('net_value', 'mean'),
    total_net_value=('net_value', 'sum')
)
top_segment_by_net = segment_summary['total_net_value'].idxmax()

print("--- 4. Segment-Level Summary ---")
print(segment_summary)
print(
    f"\nSegment contributing the most total net value: {top_segment_by_net}"
    f" (₹{segment_summary.loc[top_segment_by_net, 'total_net_value']})"
)