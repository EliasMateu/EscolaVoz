export interface AuthResponse {
  access: string
  refresh: string
  profile: 'admin' | 'funcionario'
  school_id: number | null
}