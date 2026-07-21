// Ported from @seamapi/nextlove-sdk-generator lib/custom-resource-name-conversions.ts.

export function convertCustomResourceName(responseType: string): string {
  return responseType === 'event' ? 'seam_event' : responseType
}
