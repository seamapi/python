// TEMPORARY: Verbatim port of @seamapi/nextlove-sdk-generator
// lib/endpoint-rules.ts. These lists only preserve legacy generated output:
// the ignored paths reproduce the previous endpoint filtering, and the
// deprecated action attempt list keeps those endpoints returning None.
// TODO: Delete this file once generated output is allowed to change; filter
// on blueprint undocumented flags instead and let the deprecated endpoints
// return their real response types.

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
