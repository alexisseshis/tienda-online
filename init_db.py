"""Crea las tablas y agrega productos de demostración si la base está vacía.

Este script NO borra tablas ni datos existentes.
"""

from app import app
from sqlalchemy import text
from models import db, Producto, ProductoDigital, ProductoFisico, ProductoPerecible


with app.app_context():
    db.create_all()
    db.session.execute(
        text(
            "ALTER TABLE productos "
            "ADD COLUMN IF NOT EXISTS imagen VARCHAR(255)"
        )
    )
    db.session.execute(
        text(
            "UPDATE productos SET imagen = 'default_product.svg' "
            "WHERE imagen IS NULL OR imagen = ''"
        )
    )
    catalogo_actualizado = {
        "FIS001": ("Estacion Aurora", "aurora-workstation.svg"),
        "FIS002": ("Teclado Nebula", "nebula-keyboard.svg"),
        "FIS003": ("Mouse Vector Pro", "vector-mouse.svg"),
        "FIS004": ("Silla Orbit", "orbit-chair.svg"),
        "DIG001": ("Academia Python Prisma", "prisma-python.svg"),
        "PER001": ("Canasta Frutal", "canasta-frutal.svg"),
    }
    for codigo, (nombre, imagen) in catalogo_actualizado.items():
        db.session.execute(
            text(
                "UPDATE productos SET nombre = :nombre, imagen = :imagen "
                "WHERE codigo = :codigo"
            ),
            {"codigo": codigo, "nombre": nombre, "imagen": imagen},
        )
    db.session.commit()
    print("Tablas verificadas/creadas correctamente.")

    if Producto.query.count() == 0:
        productos = [
            ProductoFisico(
                codigo="FIS001",
                nombre="Estacion Aurora",
                precio_base=1250.00,
                stock=6,
                peso_kg=8.0,
                costo_envio_por_kg=1.50,
                imagen="aurora-workstation.svg",
            ),
            ProductoFisico(
                codigo="FIS002",
                nombre="Teclado Nebula",
                precio_base=79.99,
                stock=18,
                peso_kg=0.9,
                costo_envio_por_kg=1.50,
                imagen="nebula-keyboard.svg",
            ),
            ProductoFisico(
                codigo="FIS003",
                nombre="Mouse Vector Pro",
                precio_base=89.99,
                stock=12,
                peso_kg=0.25,
                costo_envio_por_kg=1.50,
                imagen="vector-mouse.svg",
            ),
            ProductoFisico(
                codigo="FIS004",
                nombre="Silla Orbit",
                precio_base=219.00,
                stock=5,
                peso_kg=17.0,
                costo_envio_por_kg=1.50,
                imagen="orbit-chair.svg",
            ),
            ProductoDigital(
                codigo="DIG001",
                nombre="Academia Python Prisma",
                precio_base=40.00,
                stock=999,
                licencia="personal",
                imagen="prisma-python.svg",
            ),
            ProductoPerecible(
                codigo="PER001",
                nombre="Canasta Frutal",
                precio_base=8.00,
                stock=15,
                dias_para_vencer=2,
                imagen="canasta-frutal.svg",
            ),
        ]
        db.session.add_all(productos)
        db.session.commit()
        print("Productos de demostración insertados.")
    else:
        print("La tabla productos ya tiene datos; no se insertaron ejemplos.")
