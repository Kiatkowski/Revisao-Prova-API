import requests

def obter_dados_meteorologicos():
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": -26.4851,
        "longitude": -49.0713,
        "current": ["temperature_2m","relative_humidity_2m","wind_speed_10m","precipitation","apparent_temperature"],
        "timezone": "America/Sao_Paulo"
    }
    resposta = requests.get(url, params=params, timeout=15)

    dados = resposta.json()
    condicoes_atuais = dados["current"]

    return{
        "Temperatura" : condicoes_atuais["temperature_2m"],
        "Umidade_rel" : condicoes_atuais["relative_humidity_2m"],
        "Vel_Vento_10M" : condicoes_atuais["wind_speed_10m"],
        "Precipitacao" : condicoes_atuais["precipitation"],
        "Sensacao" : condicoes_atuais["apparent_temperature"]
    }
