from flask import Flask, render_template, request, redirect, url_for
import os
import joblib
import pandas as pd

app = Flask(__name__)

# Helper to load model safely
def safe_load(path):
    if not os.path.exists(path):
        return None
    try:
        return joblib.load(path)
    except Exception as e:
        print(f"Error loading {path}: {e}")
        return None

# Preload models if available (lazy load as fallback)
MODELS = {
    'hero_model': None,
    'hero_pipeline': None,
    'genre_model': None,
    'genre_pipeline': None,
    'title_model': None,
    'title_pipeline': None,
    'runtime_model': None,
    'hero_from_title_model': None,
}

def ensure_models():
    # map filenames from workspace
    base = os.path.dirname(__file__)
    MODELS['hero_model'] = MODELS['hero_model'] or safe_load(os.path.join(base, '1_model.pkl'))
    MODELS['hero_pipeline'] = MODELS['hero_pipeline'] or safe_load(os.path.join(base, '1_heroname.pkl'))
    MODELS['genre_model'] = MODELS['genre_model'] or safe_load(os.path.join(base, '2_model.pkl'))
    MODELS['genre_pipeline'] = MODELS['genre_pipeline'] or safe_load(os.path.join(base, '2_genre.pkl'))
    MODELS['title_model'] = MODELS['title_model'] or safe_load(os.path.join(base, '3_model.pkl'))
    MODELS['title_pipeline'] = MODELS['title_pipeline'] or safe_load(os.path.join(base, '3_title.pkl'))
    MODELS['runtime_model'] = MODELS['runtime_model'] or safe_load(os.path.join(base, '4_model.pkl'))
    MODELS['hero_from_title_model'] = MODELS['hero_from_title_model'] or safe_load(os.path.join(base, '5_model.pkl'))

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    choice = request.form.get('choice')
    query = request.form.get('query')
    if not choice or not query:
        return render_template('index.html', error='Please provide both choice and query.')

    ensure_models()

    try:
        if choice == 'Hero':
            if MODELS['hero_model'] is None or MODELS['hero_pipeline'] is None:
                return render_template('index.html', error='Hero model or pipeline not available on server.')
            df = pd.DataFrame([[query]], columns=['hero_name'])
            final = MODELS['hero_pipeline'].transform(df)
            pred = MODELS['hero_model'].predict(final)
            movie = pred[0]
            # title -> other attributes
            result = {'movie': movie}
            if MODELS['title_model'] and MODELS['title_pipeline']:
                tdf = pd.DataFrame([[movie]], columns=['title_x'])
                tfinal = MODELS['title_pipeline'].transform(tdf)
                pred_title = MODELS['title_model'].predict(tfinal)
                # prediction might be array-like: runtime/budget/revenue/vote_count
                try:
                    # handle different shapes
                    if hasattr(pred_title[0], '__len__'):
                        result['budget'] = pred_title[0][0]
                        result['revenue'] = pred_title[0][1]
                        result['vote_count'] = pred_title[0][2]
                except Exception:
                    pass
            if MODELS['runtime_model'] and MODELS['title_pipeline']:
                try:
                    tdf = pd.DataFrame([[movie]], columns=['title_x'])
                    tfinal = MODELS['title_pipeline'].transform(tdf)
                    pred_runtime = MODELS['runtime_model'].predict(tfinal)
                    result['runtime'] = float(pred_runtime[0])
                except Exception:
                    pass

        else:  # Genre
            if MODELS['genre_model'] is None or MODELS['genre_pipeline'] is None:
                return render_template('index.html', error='Genre model or pipeline not available on server.')
            df = pd.DataFrame([[query]], columns=['genres'])
            final = MODELS['genre_pipeline'].transform(df)
            pred = MODELS['genre_model'].predict(final)
            movie = pred[0]
            result = {'movie': movie}
            if MODELS['title_model'] and MODELS['title_pipeline']:
                try:
                    tdf = pd.DataFrame([[movie]], columns=['title_x'])
                    tfinal = MODELS['title_pipeline'].transform(tdf)
                    pred_title = MODELS['title_model'].predict(tfinal)
                    if hasattr(pred_title[0], '__len__'):
                        result['budget'] = pred_title[0][0]
                        result['revenue'] = pred_title[0][1]
                        result['vote_count'] = pred_title[0][2]
                except Exception:
                    pass
            if MODELS['runtime_model'] and MODELS['title_pipeline']:
                try:
                    tdf = pd.DataFrame([[movie]], columns=['title_x'])
                    tfinal = MODELS['title_pipeline'].transform(tdf)
                    pred_runtime = MODELS['runtime_model'].predict(tfinal)
                    result['runtime'] = float(pred_runtime[0])
                except Exception:
                    pass
            if MODELS['hero_from_title_model'] and MODELS['title_pipeline']:
                try:
                    tdf = pd.DataFrame([[movie]], columns=['title_x'])
                    tfinal = MODELS['title_pipeline'].transform(tdf)
                    pred_hero = MODELS['hero_from_title_model'].predict(tfinal)
                    result['actor'] = pred_hero[0]
                except Exception:
                    pass

        return render_template('index.html', result=result)

    except Exception as e:
        return render_template('index.html', error=str(e))


if __name__ == '__main__':
    app.run(debug=True)
