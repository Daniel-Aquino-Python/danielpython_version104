def evaluar_candidato(candidato):
    experiencia = candidato.get("experiencia", 0)
    edad = candidato.get("edad", 0)
    idiomas = candidato.get("idiomas", [])
    nivel_educacion = candidato.get("educacion", "").lower()

    # Condicionales anidados + operadores lógicos
    if experiencia >= 5 and edad < 40:
        if "inglés" in idiomas and nivel_educacion in ["maestría", "doctorado"]:
            resultado = "Altamente calificado"
        elif "inglés" in idiomas or "alemán" in idiomas:
            resultado = "Calificado"
        else:
            resultado = "Requiere mejora en idiomas"
    elif experiencia >= 2:
        resultado = "Prometedor" if edad < 30 else "Considerar para otro puesto"
    else:
        resultado = "Rechazado"

    # Uso de match-case (Python 3.10+)
    match resultado:
        case "Altamente calificado":
            recomendacion = "Avanzar a entrevista final"
        case "Calificado":
            recomendacion = "Entrevista técnica"
        case "Prometedor":
            recomendacion = "Entrevista inicial"
        case "Considerar para otro puesto":
            recomendacion = "Redirigir a vacante junior"
        case _:
            recomendacion = "Enviar notificación de rechazo"

    return f"Resultado: {resultado} | Acción: {recomendacion}"

# 🧪 Prueba
candidato1 = {
    "experiencia": 6,
    "edad": 32,
    "idiomas": ["inglés", "español"],
    "educacion": "Maestría"
}

print(evaluar_candidato(candidato1))
