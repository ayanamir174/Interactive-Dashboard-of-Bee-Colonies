# 🐝 Interactive Dashboard of Bee Colonies

> This project is an interactive web dashboard built with **Dash**, **Plotly**, and **Pandas**.  
> It visualizes the percentage of bee colonies in the United States affected by **Varroa mites** — one of the leading threats to bee health.

---

## 📄 Project Summary

👉 [**View Slide Deck (PDF)**](./Project%20Summary.pdf)

---

## 📊 Dashboard Features

- Dropdown menu to select year (2015–2018)
- Color-coded choropleth map of the United States showing % of colonies impacted
- Real-time interactive tooltips and hover info by state
- Clean and responsive UI built with Dash + Plotly

---

## 🧪 Tools & Technologies

| Tool     | Description                          |
|----------|--------------------------------------|
| Python   | Primary language                     |
| Pandas   | Data wrangling and manipulation      |
| Plotly   | Graphical visualizations             |
| Dash     | Interactive web dashboard framework  |

---

## 🔁 Data Pipeline

1. **Data Source**: Loaded USDA bee colony dataset (`intro_bees.csv`)
2. **Cleaning & Grouping**: Aggregated by year, state, and cause
3. **Filtering**: Focused on cases where cause was *Varroa mites*
4. **Visualization**: Created choropleth map for % of colonies affected
5. **Deployment**: Built and served via Dash using `bee_colonies.py`

---

## ✅ Key Insight

Between **2015–2018**, **Varroa mites** consistently impacted 20–50% of bee colonies across several U.S. states.  
This dashboard offers researchers, policymakers, and environmentalists a fast way to spot trends over time and geography.

---

## 📁 Files

| File Name                      | Description                                |
|-------------------------------|--------------------------------------------|
| `Project Summary.pdf` | Project summary slide deck (PDF)         |
| `bee_colonies.py`             | Main Dash app source code                  |
| `intro_bees.csv`              | USDA bee colony dataset                    |
| `requirements.txt`              | Python dependencies (Pandas, Dash, Plotly)|

