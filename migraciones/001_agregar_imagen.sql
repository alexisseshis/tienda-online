-- Migración manual para una base creada con las semanas 1-3 del tutorial.
-- Ejecutar una sola vez sobre la base tienda_online existente.

ALTER TABLE productos
ADD COLUMN IF NOT EXISTS imagen VARCHAR(255);

UPDATE productos
SET imagen = 'default_product.svg'
WHERE imagen IS NULL OR imagen = '';

ALTER TABLE productos
ALTER COLUMN imagen SET DEFAULT 'default_product.svg';

ALTER TABLE productos
ALTER COLUMN imagen SET NOT NULL;

-- Actualiza los productos de demostracion existentes al nuevo catalogo.
UPDATE productos
SET nombre = 'Estacion Aurora', imagen = 'aurora-workstation.svg'
WHERE codigo = 'FIS001';

UPDATE productos
SET nombre = 'Teclado Nebula', imagen = 'nebula-keyboard.svg'
WHERE codigo = 'FIS002';

UPDATE productos
SET nombre = 'Mouse Vector Pro', imagen = 'vector-mouse.svg'
WHERE codigo = 'FIS003';

UPDATE productos
SET nombre = 'Silla Orbit', imagen = 'orbit-chair.svg'
WHERE codigo = 'FIS004';

UPDATE productos
SET nombre = 'Academia Python Prisma', imagen = 'prisma-python.svg'
WHERE codigo = 'DIG001';

UPDATE productos
SET nombre = 'Canasta Frutal', imagen = 'canasta-frutal.svg'
WHERE codigo = 'PER001';
