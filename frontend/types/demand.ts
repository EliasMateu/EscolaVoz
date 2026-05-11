export type DemandStatus = 'open' | 'in_progress' | 'resolved' | 'rejected'

export interface Demand {
  id: number
  school: number
  school_name: string
  category: number
  category_name: string
  description: string
  status: DemandStatus
  employee: number
  employee_name: string
  created_at: string
  updated_at: string
}

export interface DemandCreate {
  category: number
  description: string
}

export interface PaginatedResponse<T> {
  count: number
  next: string | null
  previous: string | null
  results: T[]
}