-- VELOOP Task 01 SQL analysis (SQLite-compatible).
-- SIMULATED assignment data only. Task 02 excluded. Not production metrics.
-- Run Python script first to create task01_local_analysis.sqlite.

-- 1. Row count, unique IDs and missing IDs
SELECT COUNT(*) AS row_count, COUNT(DISTINCT user_id) AS distinct_user_ids,
 SUM(CASE WHEN user_id IS NULL OR TRIM(user_id)='' THEN 1 ELSE 0 END) AS missing_user_ids
FROM task01_users_clean;

-- 2. Duplicate user ID extra rows
SELECT COUNT(*) AS duplicate_extra_rows FROM (
 SELECT user_id, ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY user_id) rn
 FROM task01_users_clean WHERE user_id IS NOT NULL
) d WHERE rn>1;

-- 3. Missingness in selected key fields
SELECT 'registration_datetime' field_name,
 SUM(CASE WHEN registration_datetime IS NULL OR TRIM(CAST(registration_datetime AS TEXT))='' THEN 1 ELSE 0 END) missing_rows
FROM task01_users_clean
UNION ALL SELECT 'account_status',
 SUM(CASE WHEN account_status IS NULL OR TRIM(account_status)='' THEN 1 ELSE 0 END) FROM task01_users_clean
UNION ALL SELECT 'email_verification_status',
 SUM(CASE WHEN email_verification_status IS NULL OR TRIM(email_verification_status)='' THEN 1 ELSE 0 END) FROM task01_users_clean
UNION ALL SELECT 'onboarding_status',
 SUM(CASE WHEN onboarding_status IS NULL OR TRIM(onboarding_status)='' THEN 1 ELSE 0 END) FROM task01_users_clean;

-- 4. Account status distribution
SELECT COALESCE(account_status,'(Missing)') account_status, COUNT(*) user_count,
 ROUND(100.0*COUNT(*)/(SELECT COUNT(*) FROM task01_users_clean),2) pct_of_rows
FROM task01_users_clean GROUP BY 1 ORDER BY user_count DESC;

-- 5. Onboarding status by account status
SELECT COALESCE(account_status,'(Missing)') account_status,
 COALESCE(onboarding_status,'(Missing)') onboarding_status, COUNT(*) user_count
FROM task01_users_clean GROUP BY 1,2 ORDER BY 1,3 DESC;

-- 6. Acquisition source profile
SELECT COALESCE(acquisition_source,'(Missing)') acquisition_source, COUNT(*) user_count
FROM task01_users_clean GROUP BY 1 ORDER BY user_count DESC;

-- 7. Descriptive age and activity profile (not retention KPIs)
SELECT COUNT(age) non_null_age_rows, MIN(age) min_age, MAX(age) max_age,
 ROUND(AVG(age),2) average_age, ROUND(AVG(lifetime_sessions),2) avg_lifetime_sessions,
 ROUND(AVG(active_days),2) avg_active_days FROM task01_users_clean;

-- 8. Compare clean and audit sheets
SELECT 'clean' source_sheet, COUNT(*) rows, COUNT(DISTINCT user_id) distinct_user_ids FROM task01_users_clean
UNION ALL SELECT 'messy_audit', COUNT(*), COUNT(DISTINCT user_id) FROM task01_users_messy_audit;
