export interface UserProfile {
  uid: string
  email: string
  displayName: string | null
  role: 'admin' | 'researcher' | 'viewer'
  organization: string | null
  createdAt: string
}

export interface Sample {
  id: string
  name: string
  type: string
  status: 'pending' | 'processing' | 'completed' | 'failed'
  collectedAt: string
  processedAt: string | null
  ownerId: string
  metadata: Record<string, unknown>
}

export interface AnalysisResult {
  id: string
  sampleId: string
  resultType: string
  value: number
  unit: string
  referenceRange: string | null
  flagged: boolean
  createdAt: string
}

export interface DashboardStats {
  totalSamples: number
  pendingSamples: number
  completedSamples: number
  flaggedResults: number
}
