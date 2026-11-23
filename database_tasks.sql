-- Задание 1.
-- Список логинов курьеров с количеством их заказов в статусе «В доставке»
-- (поле inDelivery = true).

SELECT
    c.login,
    COUNT(o.id) AS orders_in_delivery
FROM "Couriers" c
LEFT JOIN "Orders" o
    ON o."courierId" = c.id
   AND o."inDelivery" = true
GROUP BY c.login
ORDER BY orders_in_delivery DESC;


-- Задание 2.
-- Все трекеры заказов и их статусы.
-- finished = true        -> статус 2
-- cancelled = true       -> статус -1
-- inDelivery = true      -> статус 1
-- остальные случаи       -> статус 0

SELECT
    o.track,
    CASE
        WHEN o."finished"   = true THEN 2
        WHEN o."cancelled"  = true THEN -1
        WHEN o."inDelivery" = true THEN 1
        ELSE 0
    END AS status
FROM "Orders" o
ORDER BY o.track;