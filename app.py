from flask import Flask, render_template, send_file

import requests

app = Flask(__name__)

@app.route('/health')
def health():
    return "OK"

@app.route('/report')
def report():
    data = {
        'title': 'MTG CSV Generator - Report',
        'sitename': 'http://joaomarcuslf.com',
        'repo': 'https://github.com/joaomarcuslf2/mtg-csv-generator',
        'colab': 'https://colab.research.google.com/github/joaomarcuslf2/mtg-csv-generator/blob/main/report_with_mtg_csv.ipynb',
        'csv': 'https://github.com/joaomarcuslf2/mtg-csv-generator/blob/main/files/mtg-card-list-2020-10-22.csv',
        'plots': [
            {
                'title': 'Card types drawn by Magali Villeneuve',
                'subtitle': 'The goal of this plot was to generate an bar graph with all types made by Magali Villeneuve, which is my favorite artist of MTG, I had to use some logic to extract the separators of the Type lines.',
                'img': '/https://raw.githubusercontent.com/joaomarcuslf2/mtg-csv-generator/main/report/magali-types-graph.png',
                'alt': 'Bar graph containing card types'
            },
            {
                'title': 'Comparation between types that are unique',
                'subtitle': 'The goal of this plot was to generate an bar graph with the amount of unique and not unique types for comparation.',
                'img': '/https://raw.githubusercontent.com/joaomarcuslf2/mtg-csv-generator/main/report/unique-card-types.png',
                'alt': 'Bar graph containing unique card types'
            },
            {
                'title': 'Artists that drawn 150 or above cards',
                'subtitle': 'Some artist have drawn more cards than others, but i\'ve made a couple of visualizations to see the difference between then.',
                'img': '/https://raw.githubusercontent.com/joaomarcuslf2/mtg-csv-generator/main/report/artist-arts-above-150.png',
                'alt': 'Bar graph containing artists and the number of cards drawn'
            },
            {
                'title': 'Artists that drawn between 150 and 100',
                'subtitle': 'Some artist have drawn more cards than others, but i\'ve made a couple of visualizations to see the difference between then.',
                'img': '/https://raw.githubusercontent.com/joaomarcuslf2/mtg-csv-generator/main/report/artist-arts-between-150-100.png',
                'alt': 'Bar graph containing artists and the number of cards drawn'
            },
            {
                'title': 'Artists that drawn between 100 and 75',
                'subtitle': 'Some artist have drawn more cards than others, but i\'ve made a couple of visualizations to see the difference between then.',
                'img': '/https://raw.githubusercontent.com/joaomarcuslf2/mtg-csv-generator/main/report/artist-arts-between-100-75.png',
                'alt': 'Bar graph containing artists and the number of cards drawn'
            },
            {
                'title': 'Artists that drawn between 75 and 50',
                'subtitle': 'Some artist have drawn more cards than others, but i\'ve made a couple of visualizations to see the difference between then.',
                'img': '/https://raw.githubusercontent.com/joaomarcuslf2/mtg-csv-generator/main/report/artist-arts-between-75-50.png',
                'alt': 'Bar graph containing artists and the number of cards drawn'
            },
        ]
    }

    return render_template('report.html', data=data)

@app.route('/download')
def download():
    filename = 'mtg-card-list-2020-10-22.csv'
    return send_file(
        'files/' + filename,
        mimetype='text/csv',
        attachment_filename=filename,
        as_attachment=True
    )

if __name__ == '__main__':
    app.run(debug=True)