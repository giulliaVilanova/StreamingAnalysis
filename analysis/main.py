import pandas as pd
import os

def analyze_platform(path, name):
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Data file not found: {path}\n"
            f"Please ensure the file exists at the specified location."
        )
    
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip().str.lower()

    genres = df['listed_in'].dropna().str.split(',').explode().str.strip()
    ratings = df['rating'].dropna()
    years = df['release_year'].dropna().astype(int)
    countries = df['country'].dropna().str.split(',').explode().str.strip()

    return {
        "Plataforma": name,
        "Gênero mais frequente": genres.value_counts().idxmax(),
        "Rating mais comum": ratings.value_counts().idxmax(),
        "Ano com mais lançamentos": years.value_counts().idxmax(),
        "País predominante": countries.value_counts().idxmax(),
        "Total de títulos": len(df)
    }

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    files = {
        "Netflix": os.path.join(script_dir, "data", "netflix_titles.csv"),
        "Disney+": os.path.join(script_dir, "data", "disney_plus_titles.csv"),
        "Amazon Prime Video": os.path.join(script_dir, "data", "amazon_prime_titles.csv")
    }

    data_dir = os.path.join(script_dir, "data")
    if not os.path.exists(data_dir):
        print(f"Error: Data directory not found at: {data_dir}")
        print(f"Please create the directory and add the required CSV files:")
        for name, path in files.items():
            print(f"  - {os.path.basename(path)}")
        return

    missing_files = [name for name, path in files.items() if not os.path.exists(path)]
    
    if missing_files:
        print(f"Error: The following data files are missing:")
        for name in missing_files:
            print(f"  - {name}: {os.path.basename(files[name])}")
        print(f"\nPlease add them to: {data_dir}")
        return

    output_dir = os.path.join(script_dir, "output")
    os.makedirs(output_dir, exist_ok=True)
    
    results = [analyze_platform(path, name) for name, path in files.items()]

    df = pd.DataFrame(results)
    
    csv_path = os.path.join(output_dir, "summary_report.csv")
    df.to_csv(csv_path, index=False, encoding="utf-8-sig")

    md_path = os.path.join(output_dir, "summary_report.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# Relatório de Análise de Plataformas\n\n")
        for _, row in df.iterrows():
            f.write(f"## {row['Plataforma']}\n")
            for col, val in row.items():
                if col != "Plataforma":
                    f.write(f"- **{col}:** {val}\n")
            f.write("\n---\n")

    print("✅ Relatórios gerados em /output")
    print(f"   - {csv_path}")
    print(f"   - {md_path}")

if __name__ == "__main__":
    main()