SELECT position,
       AVG(contract_time) AS average_contract_time
FROM players
GROUP BY position;
