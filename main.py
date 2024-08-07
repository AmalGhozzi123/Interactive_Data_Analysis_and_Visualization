import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Function to load data from a CSV file
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Données chargées avec succès.")
        return data
    except FileNotFoundError:
        print(f"Erreur : le fichier {file_path} est introuvable.")
    except pd.errors.EmptyDataError:
        print("Erreur : le fichier est vide.")
    except pd.errors.ParserError:
        print("Erreur : problème de parsing du fichier.")
    except Exception as e:
        print(f"Erreur lors du chargement des données : {e}")
    return None

# Function to analyze and display basic statistics of the data
def analyze_data(data):
    print("Aperçu des données :")
    print(data.head())
    print("\nRésumé statistique :")
    print(data.describe())

# Function to generate and save interactive visualizations as HTML files
def generate_visualizations(data):
    # Histogram of Age distribution
    fig1 = px.histogram(data, x='Age', title="Distribution de l'Âge")
    fig1.write_html("histogram.html")
    print("Histogram saved as histogram.html")

    # Scatter plot of Age vs Salary
    fig2 = px.scatter(data, x='Age', y='Salary', title="Âge vs Salaire")
    fig2.write_html("scatter.html")
    print("Scatter plot saved as scatter.html")

    # Bar chart of average Salary by Department
    fig3 = px.bar(data, x='Department', y='Salary', title="Salaire moyen par Département", color='Department', barmode='group')
    fig3.write_html("bar_chart.html")
    print("Bar chart saved as bar_chart.html")

    # Box plot of Salary distribution by Department
    fig4 = px.box(data, x='Department', y='Salary', title="Distribution des Salaires par Département")
    fig4.write_html("box_plot.html")
    print("Box plot saved as box_plot.html")

    # Heatmap of correlations between numeric columns
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
    corr = data[numeric_columns].corr()
    fig5 = go.Figure(data=go.Heatmap(
        z=corr.values,
        x=corr.columns,
        y=corr.columns,
        colorscale='Viridis'
    ))
    fig5.update_layout(title="Heatmap des Corrélations")
    fig5.write_html("heatmap.html")
    print("Heatmap saved as heatmap.html")

def main():
    # Path to your CSV file - use a raw string to avoid escape character issues
    file_path = r"C:\Users\amalg\Desktop\mes Travail\aa\data.csv"
    
    # Load data
    data = load_data(file_path)
    
    if data is not None:
        # Analyze data
        analyze_data(data)
        
        # Generate visualizations
        generate_visualizations(data)
        
        # Option to open the visualizations in the default web browser
        import webbrowser
        webbrowser.open('histogram.html')
        webbrowser.open('scatter.html')
        webbrowser.open('bar_chart.html')
        webbrowser.open('box_plot.html')
        webbrowser.open('heatmap.html')

if __name__ == "__main__":
    main()
