# from service import CardDetection
from factory.Service import Service
from visualizator import scatter_plot, line_plot, hist_plot

CSV_FILE_PATH = 'datasets/car_data.csv'


def card_fraud_detection():
    factory_service = Service()
    service = factory_service.get_service()

    service.standardize_data()
    service.build()
    service.test_accuracy_score()

    data = [0, -1.359, -0.0727, 2.53, 1.373, -0.338, 0.4, 0.239, 0.09, 0.363, 0.090, -0.551, -0.617, -0.991, - 0.311,
            1.468, -0.470, 0.207, 0.025, 0.403, 0.251, -0.01283, 0.277, -0.1104, 0.669, 0.128, -0.189, 0.133, -0.021,
            149.62]
    service.predict(data)
    df = service.get_dataset()
    params_line_plot = dict(x='Time', y='Amount', data=df, ci=None, lw=2, color='#aa00aa', alpha=0.6)
    params_hist_plot = dict( data=df, color='red', stat='frequency', bins=4)
    params_scatter_plot = dict(x='Time', y='Amount', data=df)
    # line_plot(df, params_line_plot)
    # scatter_plot(df, params_scatter_plot)
    hist_plot(df, params_hist_plot)


card_fraud_detection()






