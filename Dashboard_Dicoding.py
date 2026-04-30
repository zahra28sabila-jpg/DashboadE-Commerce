from typing import Tuple
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os

# ======================
# LOAD DATA
# ======================
@st.cache_data
def load_data() -> pd.DataFrame:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, 'all_df.csv.gz')
    df = pd.read_csv(csv_path)

    date_columns = [
        'order_purchase_timestamp',
        'order_approved_at',
        'order_delivered_carrier_date',
        'order_delivered_customer_date',
        'order_estimated_delivery_date'
    ]

    for col in date_columns:
        df[col] = pd.to_datetime(df[col])

    return df


# ======================
# SIDEBAR
# ======================
def create_sidebar(df: pd.DataFrame) -> Tuple[pd.Timestamp, pd.Timestamp, str]:
    with st.sidebar:
        st.header("Filter Data")

        min_date = df['order_purchase_timestamp'].min().date()
        max_date = df['order_purchase_timestamp'].max().date()

        start_date, end_date = st.date_input(
            "Rentang Waktu",
            min_value=min_date,
            max_value=max_date,
            value=[min_date, max_date]
        )

        status_list = ['ALL'] + list(df['order_status'].dropna().unique())
        selected_status = st.radio("Order Status", status_list)

    return pd.Timestamp(start_date), pd.Timestamp(end_date), selected_status


# ======================
# FILTER DATA
# ======================
def filter_data(df, start_date, end_date, status):
    df_filtered = df[
        (df['order_purchase_timestamp'].dt.date >= start_date.date()) &
        (df['order_purchase_timestamp'].dt.date <= end_date.date())
    ]

    if status != 'ALL':
        df_filtered = df_filtered[df_filtered['order_status'] == status]

    return df_filtered


# ======================
# GEO DELAY ANALYSIS
# ======================
def plot_geo_delay(df):
    df_geo = df.copy()

    df_geo['delay_days'] = (
        df_geo['order_delivered_customer_date'] -
        df_geo['order_estimated_delivery_date']
    ).dt.days

    geo = df_geo.groupby(['customer_city', 'customer_state']).agg({
        'order_id': 'count',
        'delay_days': 'mean'
    }).reset_index()

    geo = geo[geo['order_id'] > 500].sort_values(by='delay_days', ascending=False)

    fig, ax = plt.subplots(figsize=(12, 6))

    sns.scatterplot(
        data=geo,
        x='order_id',
        y='delay_days',
        hue='customer_state',
        size='order_id',
        sizes=(100, 1000),
        palette='viridis',
        ax=ax
    )

    ax.axhline(0, color='red', linestyle='--')

    ax.set_title('Volume vs Delay per Kota')
    ax.set_xlabel('Jumlah Transaksi')
    ax.set_ylabel('Delay (hari)')

    ax.legend(
        title='State',
        bbox_to_anchor=(1.05, 1),  # geser ke kanan
        loc='upper left',
        borderaxespad=0.
    )

    plt.tight_layout()
    st.pyplot(fig)



# ======================
# REVIEW SCORE ANALYSIS
# ======================
def plot_review_score(df):
    product = df.groupby('product_category_name').agg({
        'review_score': 'mean',
        'order_id': 'nunique'
    }).reset_index()

    product.columns = ['category', 'avg_score', 'total_orders']

    threshold = st.slider("Threshold Review", 1.0, 5.0, 4.0)

    bad = product[product['avg_score'] < threshold].sort_values(by='avg_score')

    fig, ax = plt.subplots(figsize=(12, 8))

    sns.barplot(
        data=bad,
        x='avg_score',
        y='category',
        color='#D4A5A5',
        ax=ax
    )

    ax.axvline(threshold, color='red', linestyle='--')
    ax.set_title('Kategori dengan Review Rendah')
    ax.set_xlim(0, 5)

    for i, p in enumerate(ax.patches):
        total = bad.iloc[i]['total_orders']
        ax.annotate(
            f'n={int(total)}',
            (p.get_width(), p.get_y() + p.get_height() / 2),
            ha='left', va='center',
            xytext=(5, 0),
            textcoords='offset points'
        )

    st.pyplot(fig)


# ======================
# MONTHLY SALES
# ======================
def plot_monthly_sales(df):
    # Agregasi bulanan dari DATA HASIL FILTER
    monthly = df.groupby(
        df['order_purchase_timestamp'].dt.to_period('M')
    )['payment_value'].sum().reset_index()

    monthly['order_purchase_timestamp'] = monthly[
        'order_purchase_timestamp'
    ].dt.to_timestamp()

    monthly = monthly.sort_values('order_purchase_timestamp')

    # Hitung MoM
    monthly['mom_growth'] = monthly['payment_value'].pct_change() * 100

    # Peak
    peak_val = monthly['payment_value'].max()
    peak_month = monthly.loc[
        monthly['payment_value'].idxmax(),
        'order_purchase_timestamp'
    ].strftime('%B %Y')

    # ======================
    # PLOT
    # ======================
    fig, ax1 = plt.subplots(figsize=(14, 7))

    # Bar: Sales
    sns.barplot(
        x=monthly['order_purchase_timestamp'].dt.strftime('%b %Y'),
        y=monthly['payment_value'],
        ax=ax1
    )

    # Line: MoM
    ax2 = ax1.twinx()

    sns.lineplot(
        x=range(len(monthly)),
        y=monthly['mom_growth'],
        marker='o',
        color='red',
        linewidth=2.5,
        ax=ax2
    )

    ax2.axhline(0, color='red', linestyle='--')

    # Label
    ax1.set_xlabel('Bulan')
    ax1.set_ylabel('Total Payment')
    ax2.set_ylabel('MoM Growth (%)')

    ax1.set_title(f'Tren Penjualan Bulanan (Peak: {peak_month})')

    # 🔥 FIX legend gabungan
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines + lines2, labels + labels2, loc='upper left')

    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(fig)

    # ======================
    # SUMMARY
    # ======================
    st.write(f"**Peak Sales:** {peak_month}")
    st.write(f"**Avg MoM Growth:** {monthly['mom_growth'].mean():.2f}%")
# ======================
# MAIN APP
# ======================
def main():
    st.title("📊 Dashboard Analisis E-Commerce")

    df = load_data()

    start_date, end_date, status = create_sidebar(df)
    df_filtered = filter_data(df, start_date, end_date, status)

    st.subheader("📍 Geo Delay Analysis")
    plot_geo_delay(df_filtered)

    st.subheader("⭐ Review Score Analysis")
    plot_review_score(df_filtered)

    st.subheader("💰 Monthly Sales")
    plot_monthly_sales(df_filtered)


if __name__ == "__main__":
    main()