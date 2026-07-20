// Ported from @seamapi/nextlove-sdk-generator lib/endpoint-rules.ts.

export const endpointsReturningDeprecatedActionAttempt = [
  '/access_codes/delete',
  '/access_codes/unmanaged/delete',
  '/access_codes/update',
  '/noise_sensors/noise_thresholds/delete',
  '/noise_sensors/noise_thresholds/update',
  '/thermostats/climate_setting_schedules/update',
]

export const ignoredEndpointPaths = [
  '/health',
  '/health/get_health',
  '/health/get_service_health',
  '/health/service/[service_name]',
]
