import { useState } from 'react'
import { useForm } from 'react-hook-form'
import { z } from 'zod'
import { zodResolver } from '@hookform/resolvers/zod'

const schema = z.object({
  email: z.string().email('Invalid email address'),
  password: z.string().min(8, 'Password must be at least 8 characters'),
})

type FormData = z.infer<typeof schema>

interface AuthFormProps {
  mode: 'login' | 'register'
  onSubmit: (email: string, password: string) => Promise<void>
}

export default function AuthForm({ mode, onSubmit }: AuthFormProps) {
  const [error, setError] = useState<string | null>(null)
  const [submitting, setSubmitting] = useState(false)

  const { register, handleSubmit, formState: { errors } } = useForm<FormData>({
    resolver: zodResolver(schema),
  })

  const submit = async ({ email, password }: FormData) => {
    setError(null)
    setSubmitting(true)
    try {
      await onSubmit(email, password)
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'An error occurred')
    } finally {
      setSubmitting(false)
    }
  }

  return (
    <form onSubmit={handleSubmit(submit)} style={styles.form}>
      <div style={styles.field}>
        <label htmlFor="email" style={styles.label}>Email</label>
        <input id="email" type="email" {...register('email')} style={styles.input} />
        {errors.email && <span style={styles.error}>{errors.email.message}</span>}
      </div>
      <div style={styles.field}>
        <label htmlFor="password" style={styles.label}>Password</label>
        <input id="password" type="password" {...register('password')} style={styles.input} />
        {errors.password && <span style={styles.error}>{errors.password.message}</span>}
      </div>
      {error && <div style={styles.error}>{error}</div>}
      <button type="submit" disabled={submitting} style={styles.button}>
        {submitting ? 'Please wait...' : mode === 'login' ? 'Sign In' : 'Create Account'}
      </button>
    </form>
  )
}

const styles: Record<string, React.CSSProperties> = {
  form: { display: 'flex', flexDirection: 'column', gap: '1rem' },
  field: { display: 'flex', flexDirection: 'column', gap: '0.25rem' },
  label: { fontSize: '0.875rem', fontWeight: 500 },
  input: {
    padding: '0.5rem 0.75rem',
    border: '1px solid var(--color-border)',
    borderRadius: 'var(--radius)',
    fontSize: '1rem',
    outline: 'none',
  },
  error: { color: 'var(--color-error)', fontSize: '0.8rem' },
  button: {
    padding: '0.625rem 1.25rem',
    background: 'var(--color-primary)',
    color: '#fff',
    border: 'none',
    borderRadius: 'var(--radius)',
    fontSize: '1rem',
    fontWeight: 600,
  },
}
